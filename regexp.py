{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ac7df92e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Passed\n",
      "Passed\n",
      "Passed\n",
      "Failed to match the email -- hello@gmail\n"
     ]
    }
   ],
   "source": [
    "#make a regular expression that will match an email\n",
    "import re\n",
    "def test_email(pattern):\n",
    "    pattern = re.compile(pattern)\n",
    "    emails = [\"john@example.com\", \"python-list@python.org\", \"wha.t.`1an?ug{}ly@email.com\", \"hello@gmail\"]\n",
    "    for email in emails:\n",
    "        if not re.match(pattern, email):\n",
    "            print(\"Failed to match the email -- %s\" % (email))\n",
    "        elif not pattern:\n",
    "            print(\"Forgot to enter a pattern!\")\n",
    "        else:\n",
    "            print(\"Passed\")\n",
    "\n",
    "pattern = r\"\\\"?([-a-zA-Z0-9.`?{}]+@\\w+\\.\\w+)\\\"?\"\n",
    "test_email(pattern)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e835dfa",
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
