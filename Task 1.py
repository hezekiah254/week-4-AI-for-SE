{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9ce47121-9abe-4d20-9f87-d433a81d29d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorted by age (ascending):\n",
      "[{'name': 'Bob', 'age': 22, 'score': 95}, {'name': 'Alice', 'age': 25, 'score': 88}, {'name': 'David', 'age': 27, 'score': 82}, {'name': 'Charlie', 'age': 30, 'score': 78}]\n",
      "\n",
      "Sorted by score (descending):\n",
      "[{'name': 'Bob', 'age': 22, 'score': 95}, {'name': 'Alice', 'age': 25, 'score': 88}, {'name': 'David', 'age': 27, 'score': 82}, {'name': 'Charlie', 'age': 30, 'score': 78}]\n"
     ]
    }
   ],
   "source": [
    "def sort_dicts_by_key(data, key, reverse=False):\n",
    "    \"\"\"\n",
    "    Sorts a list of dictionaries by a specified key.\n",
    "\n",
    "    Parameters:\n",
    "        data (list): A list of dictionaries to sort.\n",
    "        key (str): The dictionary key to sort by.\n",
    "        reverse (bool): Set to True for descending order. Default is False (ascending).\n",
    "\n",
    "    Returns:\n",
    "        list: A new list of dictionaries sorted by the given key.\n",
    "    \"\"\"\n",
    "    try:\n",
    "        # Using Python's built-in sorted() for efficiency (Timsort - O(n log n))\n",
    "        sorted_data = sorted(data, key=lambda item: item[key], reverse=reverse)\n",
    "        return sorted_data\n",
    "    except KeyError:\n",
    "        print(f\"Error: Key '{key}' not found in one or more dictionaries.\")\n",
    "        return data\n",
    "    except TypeError:\n",
    "        print(\"Error: Invalid data format. Ensure 'data' is a list of dictionaries.\")\n",
    "        return data\n",
    "\n",
    "\n",
    "# Example usage:\n",
    "if __name__ == \"__main__\":\n",
    "    people = [\n",
    "        {\"name\": \"Alice\", \"age\": 25, \"score\": 88},\n",
    "        {\"name\": \"Bob\", \"age\": 22, \"score\": 95},\n",
    "        {\"name\": \"Charlie\", \"age\": 30, \"score\": 78},\n",
    "        {\"name\": \"David\", \"age\": 27, \"score\": 82}\n",
    "    ]\n",
    "\n",
    "    print(\"Sorted by age (ascending):\")\n",
    "    print(sort_dicts_by_key(people, \"age\"))\n",
    "\n",
    "    print(\"\\nSorted by score (descending):\")\n",
    "    print(sort_dicts_by_key(people, \"score\", reverse=True))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6c855d8-130d-4aaa-b47e-6f45e690703d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
