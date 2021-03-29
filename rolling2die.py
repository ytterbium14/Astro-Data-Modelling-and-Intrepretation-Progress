{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter number of events 100\n",
      "[2, 10, 9, 12, 12, 5, 9, 4, 2, 9, 5, 10, 4, 9, 5, 10, 2, 5, 3, 4, 3, 4, 5, 1, 1, 6, 8, 8, 8, 11, 8, 2, 2, 7, 7, 11, 12, 4, 9, 3, 9, 12, 7, 7, 1, 5, 5, 5, 7, 11, 10, 11, 9, 11, 4, 6, 9, 7, 12, 6, 4, 5, 2, 10, 5, 3, 8, 3, 11, 6, 5, 2, 11, 8, 10, 9, 2, 11, 11, 5, 12, 3, 8, 4, 7, 11, 10, 1, 1, 9, 7, 7, 6, 10, 3, 1, 6, 12, 6, 2]\n",
      "[0, 6, 9, 7, 8, 12, 7, 9, 7, 10, 8, 10, 7, 0]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "import random\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "n=int(input(\"enter number of events \"))\n",
    "value=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]\n",
    "sum=[]\n",
    "\n",
    "for i in range(n):\n",
    "    sum.append(random.randint(1,12))\n",
    "    \n",
    "for i in range(0,len(sum)):\n",
    "    t=sum[i]\n",
    "    value[t]+=1\n",
    "    \n",
    "    \n",
    "print(sum)\n",
    "print(value)\n",
    "plt.hist(sum,bins=[1,2,3,4,5,6,7,8,9,10,11,12])\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
