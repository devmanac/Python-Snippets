{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8e28ca01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[34, 44, 68, 44, 12]\n"
     ]
    }
   ],
   "source": [
    "numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]\n",
    "newlist = [int(x) for x in numbers if x > 0]\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "146da406",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hello,', 'i', 'am', 'here,', 'you', 'are', 'there.', '*stop*']\n",
      "[6, 1, 2, 5, 3, 3, 6]\n"
     ]
    }
   ],
   "source": [
    "sentence = \"hello, i am here, you are there. *stop*\"\n",
    "words = sentence.split()\n",
    "word_lengths = [len(word) for word in words if word != \"*stop*\"]\n",
    "print(words)\n",
    "print(word_lengths)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37f54857",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
