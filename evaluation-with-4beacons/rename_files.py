import os


def rename_csv_files(directory):
    """
  This function parses a directory and renames all the CSV files incrementally.

  Args:
    directory: The path to the directory containing the CSV files.
  """
    counter = 1
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            old_path = os.path.join(directory, filename)
            new_filename = f"{str(counter)}.csv"
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            counter += 1


# Example usage
directory1 = "./groundtruths"
directory2 = "./inertials"
directory3 = "corrected_trajectories"
rename_csv_files(directory1)
rename_csv_files(directory2)
rename_csv_files(directory3)

print("CSV files renamed successfully!")
