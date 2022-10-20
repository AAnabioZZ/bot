from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *

app = ApplicationBuilder().token("5502983826:AAHqnDHCxzwFkZeJI08dxeLk0XNniSUrbMY").build()



app.add_handler(CommandHandler("hi", bot_hi))
app.add_handler(CommandHandler("time", bot_time))
app.add_handler(CommandHandler("help", bot_help))
# app.add_handler(CommandHandler("sum", bot_sum()))





print("start server")
app.run_polling()




# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# list = [1,2,3,4,3,2,3,2,4,5,6,4,5,3]
# plt.plot(list)

# plt.show()



# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))







# from progress.bar import Bar
# import time 
# with Bar('Processing', max=20) as bar:
#     for i in range(20):
#         time.sleep(0.3)
#         bar.next()







# from isOdd import isOdd

# print(isOdd(1)) 
# print(isOdd(2)) 