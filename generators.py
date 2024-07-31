{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c8501fc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n",
      "55\n"
     ]
    }
   ],
   "source": [
    "# fibonacci series with generator\n",
    "def fib():\n",
    "    a, b = 1, 1\n",
    "    while 1:\n",
    "        yield a\n",
    "        a, b = b, a + b\n",
    "\n",
    "# testing code\n",
    "import types\n",
    "\n",
    "counter = 0\n",
    "for n in fib():\n",
    "    print(n)\n",
    "    counter += 1\n",
    "    if counter == 10:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9fa0cc2",
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
