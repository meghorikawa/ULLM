class IterDialog:
  """
  An Iterator to go through all the messages in a dialog dataframe and
  output the history of the corresponding dialog as a list of messages,
  with the interaction in question as the last index
  """

  def __init__(self, df):
    """
    Initialize the iterator with the dataframe and the pointer as the index of 
    the first row
    """
    self.df = df
    self.pointer = df.index[0]

  def __next__(self):
    """
    Gets the history of the next message in the dataframe. The message in question
    is the last item in the returned list. 
    """  
    history = []
    row = self.df.loc[self.pointer]
    cur_id = row['dialog_id']
    # a smaller df containing only the current conversation 
    cur_dialog_df = self.df[(self.df['dialog_id'] == cur_id)]

    # if there are rows with a lower index and the same dialog_id, those messages came first. Add those to the history.
    for _, prev_row in cur_dialog_df[cur_dialog_df.index < self.pointer].iterrows():
        history.append(f"BOT: {prev_row['bot_elicitation']}")
        history.append(f"STUDENT: {prev_row['user_input']}")

    # add bot_elicitation and user input at current point
    history.append(f"BOT: {row['bot_elicitation']}")
    history.append(f"STUDENT: {row['user_input']}")

    self.pointer += 1
    return history

  def __len__(self):
      return len(self.df)

  def __iter__(self):
    return self
