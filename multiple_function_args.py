{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "67b732b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Extra 1 Agument. Good.\n",
      "Extra 2 Aguments. Better.\n",
      "Addition Result -->  30\n",
      "Mutiplication Result -->  750\n"
     ]
    }
   ],
   "source": [
    "def check(a, b, c, *extra_args):\n",
    "    return len(list(extra_args))\n",
    "\n",
    "def do(a, b, c, **op):\n",
    "    if op.get(\"operation\") == 'multiply':\n",
    "        return a * b * c\n",
    "    elif op.get(\"operation\") == 'add':\n",
    "        return a + b + c\n",
    "    else: \n",
    "        return nan\n",
    "        \n",
    "# test code\n",
    "if check(10, 20, 30, 40) == 1:\n",
    "    print(\"Extra 1 Agument. Good.\")\n",
    "if check(1, 2, 3, 4, 5) == 2:\n",
    "    print(\"Extra 2 Aguments. Better.\")\n",
    "result = do(5, 10, 15, operation='add')\n",
    "print(\"Addition Result --> \", result)\n",
    "result = do(5, 10, 15, operation='multiply')\n",
    "print(\"Mutiplication Result --> \", result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb86bd5f",
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