import read_annotations as reader
import pandas as pd


if __name__ == "__main__":
    # Read in data
    df = pd.read_csv('DataAnnotation_030924.csv')
    print("data read in")
    # Drop unnecessary columns
    df = df.drop(columns=['Annotator', 'Raw Data Link: ', 'ULLMs data'])

    # split df into two dfs with messages belonging to the two different tasks: "Comparing Athletes" and "Buying a Birthday Present"
    mask = df['task'] == "Comparing Athletes"
    athletes_df = df[mask]
    bday_df = df[~mask]

    athletes_iter = reader.IterDialog(athletes_df)

    for i in range(0, len(athletes_iter)):
        print(next(athletes_iter))