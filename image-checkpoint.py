{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Grade:\n",
    "    #constructor will pass the parameters to the CalGrade function\n",
    "    def __init__(self, first, second, third,\n",
    "                 fourth, fifth):\n",
    "        \n",
    "        self.first = first\n",
    "        self.second = second\n",
    "        self.third = third\n",
    "        self.fourth = fourth\n",
    "        self.fifth = fifth\n",
    "    \n",
    "    def CalGrade(self):\n",
    "        \n",
    "       #Average is calculated\n",
    "        average = (self.first + self.second + self.third\n",
    "                            + self.fourth + self.fifth)/ 5\n",
    "        \n",
    "        print(\" Your average is \", average)\n",
    "        \n",
    "        #average is checked for evaluating the Grade of the student\n",
    "        if (90 <= average <= 100) :\n",
    "\n",
    "            print(\" You have obtained Grade A \")\n",
    "\n",
    "        elif  (80 <= average < 90) :\n",
    "\n",
    "            print(\" You have obtained Grade B \")\n",
    "\n",
    "        elif (70 <= average < 80) :\n",
    "\n",
    "            print(\" You have obtained Grade C \")\n",
    "\n",
    "        elif  (60 <= average < 70) :\n",
    "\n",
    "            print(\" You have obtained Grade D \")\n",
    "\n",
    "        else:\n",
    "\n",
    "            print(\" You have obtained Grade F \")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    \n",
    "    first = int(input(\" Enter the marks obtained in first subject: \"))\n",
    "    second = int(input(\" Enter the marks obtained in second subject: \"))\n",
    "    third = int(input(\" Enter the marks obtained in third subject: \"))\n",
    "    fourth = int(input(\" Enter the marks obtained in fourth subject: \"))\n",
    "    fifth = int(input(\" Enter the marks obtained in fifth subject: \"))\n",
    "    #Object is created for class Grade\n",
    "    Grade_obj = Grade(first, second, third, fourth, fifth)\n",
    "    #CalGrade function is called\n",
    "    Grade_obj.CalGrade()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
