from tkinter.font import BOLD
import turtle as a
from tkinter import *
import pandas as pd
import numpy as np
from csv import writer
import csv
import matplotlib.pyplot as plt
from sklearn import linear_model
from scipy.stats import binom
data=pd.read_csv('sucide.csv')
index = data.index
max_row = len(index)
max_column=len(data.columns)



def do_stuff():
    app= Toplevel(canvas.master)
    app.title('huzaifa')
    app.geometry('1440x900')
    
    bg = PhotoImage(file = "D:\\Pic\\k1.jpeg")
    
    label1 = Label( app, image = bg)
    label1.place(x = 0, y = 0)
    def helloCallBack():
      newWindow = Toplevel(app)
      newWindow.title("New Window")
      newWindow.geometry("200x200")
      main_frame = Frame(newWindow)
      main_frame.pack(fill=BOTH, expand=1)
      my_canvas = Canvas(main_frame)
      my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
      my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
      my_scrollbar.pack(side=RIGHT, fill=Y)
      my_canvas.configure(yscrollcommand=my_scrollbar.set)
      my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
      second_frame = Frame(my_canvas)
      my_canvas.create_window((0,0), window=second_frame, anchor="nw")
      for r in range(max_row):
         for c in range(max_column):
             if c>2:
              Label(second_frame, text=f'{data.iloc[r][c]}',width=15, fg='blue',font=('Arial',8,BOLD)).grid(row=r, column=c, pady=10, padx=10)
             else :
              Label(second_frame, text=f'{data.iloc[r][c]}',width=25, fg='blue',font=('Arial',6,BOLD)).grid(row=r, column=c, pady=10, padx=10)
      print("done")
    
    def DATA_DELETE(): 
      def DELETE_DONE():
       global max_row
       global data
       print(max_row)
       x1=entry1_delete.get()
       print(x1)
       for r in range(max_row):
         if x1 == data.iloc[r][0]:
            data=data.drop(data.index[r])
            max_row=max_row-1
            print('hello')
            break
           
       print(data) 
       print(max_row) 
       headerList = ['Date', 'Islamic Date', 'Blast Day Type','Holiday Type','City','Province','Target Type','Killed Max','Injured Max','No. of Suicide Blasts','Explosive Weight (max)','VicTams']  
       with open('sucide.csv', 'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headerList)
            for i in range(max_row):
               writer.writerow(data.iloc[i].values)
            f.close()   
     
           

      newWindow3= Toplevel(app)
      newWindow3.title("Delete Window")
      newWindow3.geometry("300x300")
      canvas1_delete = Canvas(newWindow3, width = 400, height = 30)
      canvas1_delete.pack()
      entry1_delete = Entry (newWindow3) 
      canvas1_delete.create_window(150, 20, window=entry1_delete)
      G=Button(newWindow3,text='DELETE', command=DELETE_DONE)
      G.pack()
    def ADD_DATA():
    
      def adddone():
        global max_row
        max_row=max_row+1
        print(max_row)
        x1 = entry1.get()
        x2 = entry2.get()
        x3 = entry3.get()
        x4 = entry4.get()
        x5 = entry5.get()
        x6= entry6.get()
        x7 = entry7.get()
        x8 = int(entry8.get())
        x9 = int(entry9.get())
        x10 = int(entry10.get())
        x11 = int(entry11.get())
        x12=int(x8)+int(x9)
        list_data=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
        with open('sucide.csv', 'a', newline='') as f_object:  
      
         writer_object = writer(f_object)
    
         writer_object.writerow(list_data) 
       
         f_object.close()
      newWindow2 = Toplevel(app)
      newWindow2.title("ADD Window")
      newWindow2.geometry("300x300")
      canvas1 = Canvas(newWindow2, width = 400, height = 30)
      canvas1.pack()
      entry1 = Entry (newWindow2) 
      canvas1.create_window(200, 20, window=entry1)
      canvas2 = Canvas(newWindow2, width = 400, height = 30)
      canvas2.pack()
      entry2 = Entry (newWindow2) 
      canvas2.create_window(200, 10, window=entry2)
      canvas3 = Canvas(newWindow2, width = 400, height = 30)
      canvas3.pack()
      entry3 = Entry (newWindow2) 
      canvas3.create_window(200, 10, window=entry3)
      canvas4 = Canvas(newWindow2, width = 400, height = 30)
      canvas4.pack()
      entry4 = Entry (newWindow2) 
      canvas4.create_window(200, 10, window=entry4)
      canvas5 = Canvas(newWindow2, width = 400, height = 30)
      canvas5.pack()
      entry5 = Entry (newWindow2)
      canvas5.create_window(200, 10, window=entry5) 
      canvas6 = Canvas(newWindow2, width = 400, height = 30)
      canvas6.pack()
      entry6 = Entry (newWindow2) 
      canvas6.create_window(200, 10, window=entry6) 
      canvas7 = Canvas(newWindow2, width = 400, height = 30)
      canvas7.pack()
      entry7 = Entry (newWindow2) 
      canvas7.create_window(200, 10, window=entry7) 
      canvas8= Canvas(newWindow2, width = 400, height = 30)
      canvas8.pack()
      entry8 = Entry (newWindow2)
      canvas8.create_window(200, 10, window=entry8) 
      canvas9= Canvas(newWindow2, width = 400, height = 30)
      canvas9.pack()
      entry9 = Entry (newWindow2)
      canvas9.create_window(200, 10, window=entry9) 
      canvas10= Canvas(newWindow2, width = 400, height = 30)
      canvas10.pack()
      entry10 = Entry (newWindow2) 
      canvas10.create_window(200, 10, window=entry10) 
      canvas11= Canvas(newWindow2, width = 400, height = 30)
      canvas11.pack()
      entry11 = Entry (newWindow2)
      canvas11.create_window(200, 10, window=entry11) 
      E=Button(newWindow2,text='ADD', command=adddone)
      E.pack()

    def fun_graph():
      fun_G = Toplevel(app)
      fun_G .title("ADD Window")
      fun_G .geometry("1440x900")
      bg = PhotoImage(file = "D:\\Pic\\k1.jpeg")
      label1 = Label(fun_G, image = bg)
      label1.place(x = 0, y = 0)
      def N_D():
         dh=data['Date']
         r=[]
         l=[]
         k=""
         for i in range(len(dh)):
           k=""
           for j in range(len(dh[i])):
             if dh[i][j]=='-':
                break
             k+=dh[i][j]
           r.append(k) 
            
         plt.hist(r)
         plt.xlabel("Day ($)", labelpad=14)
         plt.ylabel("Number of Attacks", labelpad=30)
         plt.title("Number of Attacks in Day", y=1.015, fontsize=22);
         plt.show()
      def K_I():
          df_visual = pd.DataFrame(data, columns=['Date', 'Killed Max', 'Injured Max'])
          df_visual['month'] = pd.DatetimeIndex(df_visual['Date']).month
          df_visual['year'] = pd.DatetimeIndex(df_visual['Date']).year
          l=np.array(df_visual["Injured Max"])
          k=np.array(df_visual["Killed Max"])
          sum_column =np.add(l,k)
          df_visual["Victims"] = sum_column
          dfTopYear = df_visual.groupby(["year"], as_index=False).sum()
          fig = dfTopYear.plot(x="year", 
          y=["Killed Max", "Injured Max"], 
          kind="bar", 
          figsize=(15,8), align='center'
          )
          fig.set_title("Killed & Injured Per Year", pad=20, fontdict={'fontsize':24})
          plt.xticks(rotation=30, horizontalalignment="center")
          plt.xlabel("Years", fontsize=15)
          plt.ylabel("Numbers", fontsize=15)
          fig.legend(loc=1,fontsize=15)
          plt.show()
      def N_B():
          df_visual = pd.DataFrame(data, columns=['Date', 'Killed Max', 'Injured Max','No. of Suicide Blasts'])
          df_visual['month'] = pd.DatetimeIndex(df_visual['Date']).month
          df_visual['year'] = pd.DatetimeIndex(df_visual['Date']).year
          l=np.array(df_visual["Injured Max"])
          k=np.array(df_visual["Killed Max"])
          sum_column =np.add(l,k)
          df_visual["Victims"] = sum_column
          dfBlastTimeline = df_visual.groupby(["year", "month"], as_index=False).sum()
          dfBlastTimeline = dfBlastTimeline.sort_values(["year", "month"])
          
          plt.style.use("fivethirtyeight")
          dfBlastTimeline['No. of Suicide Blasts'].plot(subplots=True, figsize=(14, 8))
          plt.title("Number of Suicide Blasts")
          plt.show()
      def N_P():
        dh=data['Date']
        r=[]
        for i in range(len(dh)):
           r.append(dh[i][-4:])
        plt.figure(figsize=(8,8))
        plt.hist(data['Province'])
        plt.xlabel("Province ($)", labelpad=4)
        plt.ylabel("attacks", labelpad=10)
        plt.title("NO of attacks in province  ($)", y=1.015, fontsize=22);
        plt.show()
      def N_B_B():
            dfBlast_holiday = pd.DataFrame(data, columns=['Date', 'No. of Suicide Blasts', 'Blast Day Type', 'Holiday Type',
                                              'Killed Max', 'Injured Max'])

            dfBlast_holiday['year'] = pd.DatetimeIndex(dfBlast_holiday['Date']).year
            dfBlast_holiday['month'] = pd.DatetimeIndex(dfBlast_holiday['Date']).month
            dfBlast_holiday['victims'] =  dfBlast_holiday['Killed Max'] + dfBlast_holiday['Injured Max']
            dfBlast_holiday.drop(['Date', 'Killed Max',  'Injured Max'], axis=1, inplace = True)
            dfholiday = dfBlast_holiday.groupby(['Blast Day Type'], as_index=False).sum()
            dfholiday = dfholiday.sort_values(["No. of Suicide Blasts"], ascending=False)
            fig = dfholiday.plot(x="Blast Day Type", 
                y=["No. of Suicide Blasts"], 
                kind="bar", 
                figsize=(15,8), align='center'
                 )
            fig.set_title("Number of Blast & Blast Day Type", pad=20, fontdict={'fontsize':24})
            plt.xticks(rotation=30, horizontalalignment="center")
            plt.xlabel("Blast Day Types", fontsize=15)
            plt.ylabel("Number Of Blasts", fontsize=15)
            fig.legend(loc=1,fontsize=15)
            plt.show()
      def N_V_B():
          dfBlast_holiday = pd.DataFrame(data, columns=['Date', 'No. of Suicide Blasts', 'Blast Day Type', 'Holiday Type',
                                              'Killed Max', 'Injured Max'])
          dfBlast_holiday['year'] = pd.DatetimeIndex(dfBlast_holiday['Date']).year
          dfBlast_holiday['month'] = pd.DatetimeIndex(dfBlast_holiday['Date']).month
          dfBlast_holiday['victims'] =  dfBlast_holiday['Killed Max'] + dfBlast_holiday['Injured Max']
          dfBlast_holiday.drop(['Date', 'Killed Max',  'Injured Max'], axis=1, inplace = True)
          dfholiday = dfBlast_holiday.groupby(['Blast Day Type'], as_index=False).sum()
          dfholiday = dfholiday.sort_values(["victims"], ascending=False)
          fig = dfholiday.plot(x="Blast Day Type", 
          y=["victims"], 
          kind="bar", 
          figsize=(15,8), align='center'
          )
          fig.set_title("Number of Victims & Blast Day Type", pad=20, fontdict={'fontsize':24})
          plt.xticks(rotation=30, horizontalalignment="center")
          plt.xlabel("Blast Day Type", fontsize=15)
          plt.ylabel("Number Of Victims", fontsize=15)
          fig.legend(loc=1,fontsize=15)
          plt.show()
      def P_R():
          fun_G1= Toplevel(fun_G)
          fun_G1 .title("ADD Window")
          fun_G1 .geometry("1440x900")
          X = data[['No. of Suicide Blasts', 'Explosive Weight (max)']]
          y = data['VicTams']
          regr = linear_model.LinearRegression()
          regr.fit(X, y)
          predictedvictims = regr.predict([[1, 1]])
          Label(fun_G1,text = predictedvictims).place(x = 40,
                                           y = 60)  
           
      def B_D():
       n = 50
       p = 255/497
       x=30
       l=0
       r_values = list(range(x + 1))
       mean, var = binom.stats(n, p)
       dist = [binom.pmf(r, n, p) for r in r_values ]
       for i in range(x + 1):
         l+=dist[i]
       plt.bar(r_values, dist)
       plt.show()
       
           
      frame2 = Frame(fun_G,bg="#242424")
      frame2.pack(pady = 100,ipadx=100,ipady=150)
      E=Button(frame2,text='Number of Attacks in Day', command=N_D)
      E.pack(pady=20,ipadx=40) 
      F=Button(frame2,text='Killed & Injured Per Year', command=K_I)
      F.pack(pady=20,ipadx=40)
      G=Button(frame2,text='Number of Sucide Blast', command=N_B)
      G.pack(pady=20,ipadx=40)
      H=Button(frame2,text='NO of attacks in province ', command=N_P)
      H.pack(pady=20,ipadx=40)
      I=Button(frame2,text='Number of Blast & Blast Day Type', command=N_B_B)
      I.pack(pady=20,ipadx=40)
      J=Button(frame2,text='Number of Victims & Blast Day Type', command=N_V_B)
      J.pack(pady=20,ipadx=40)
      K=Button(frame2,text='Prediction', command=P_R)
      K.pack(pady=20,ipadx=40)
      M=Button(frame2,text='Binomial Distribution', command=B_D)
      M.pack(pady=20,ipadx=40)
      fun_G.mainloop()
      
    def fun_des():
      fun_G = Toplevel(app)
      fun_G .title("ADD Window")
      fun_G .geometry("1440x900")
      bg = PhotoImage(file = "D:\\Pic\\k1.jpeg")
      label1 = Label(fun_G, image = bg)
      label1.place(x = 0, y = 0)
      def P_R():
        fun_G1= Toplevel(fun_G)
        fun_G1 .title("ADD Window")
        fun_G1 .geometry("1440x900")
        X = data[['No. of Suicide Blasts', 'Explosive Weight (max)']]
        y = data['VicTams']
        regr = linear_model.LinearRegression()
        regr.fit(X, y)
        predictedvictims = regr.predict([[1, 1]])
        
        Label(fun_G1,text =predictedvictims,fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").place(x = 500,
                                           y = 120) 
        
      def N_V_B():
        exit()
      def N_B_B():
        exit()
      def N_P():
        exit()
      def N_B():
        exit()
      def K_I():
        fun_G1= Toplevel(fun_G)
        fun_G1 .title("ADD Window")
        fun_G1 .geometry("1440x900")
        Label(fun_G1,text ="Max No of victim in attack is Working Day",fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").place(x = 500,
                                           y = 120) 
        Label(fun_G1,text ="Min No of victim in attack is Weekend Day",fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").place(x = 500,
                                           y = 180) 
      def N_D():
        fun_G1= Toplevel(fun_G)
        fun_G1 .title("ADD Window")
        fun_G1 .geometry("1440x900")
        Label(fun_G1,text ="Highest attack in Friday and Thursday(88 attack)",fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").place(x = 500,
                                           y = 120) 
        Label(fun_G1,text ="lowest attack in Sunday.(49 attack)",fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").place(x = 500,
                                           y = 180) 
      def B_D1():
       fun_G1= Toplevel(fun_G)
       fun_G1 .title("ADD Window")
       fun_G1 .geometry("1440x900")
       n = 50
       p = 255/497
       x=30
       l=0
       r_values = list(range(x + 1))
       mean, var = binom.stats(n, p)
       dist = [binom.pmf(r, n, p) for r in r_values ]
       for i in range(x + 1):
         l+=dist[i]
       Label(fun_G1,text = l,fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").place(x = 400,
                                           y = 60) 
       Label(fun_G1,text = "mean = "+str(mean),fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").place(x = 400,
                                           y = 120) 
       Label(fun_G1,text = "variance = "+str(var),fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").place(x = 400,
                                           y = 180) 
          
      frame2 = Frame(fun_G,bg="#242424")
      frame2.pack(pady = 100,ipadx=100,ipady=150)
      E=Button(frame2,text='Number of Attacks in Day', command=N_D)
      E.pack(pady=20,ipadx=40) 
      F=Button(frame2,text='Killed & Injured Per Year', command=K_I)
      F.pack(pady=20,ipadx=40)
      G=Button(frame2,text='Number of Sucide Blast', command=N_B)
      G.pack(pady=20,ipadx=40)
      H=Button(frame2,text='NO of attacks in province ', command=N_P)
      H.pack(pady=20,ipadx=40)
      I=Button(frame2,text='Number of Blast & Blast Day Type', command=N_B_B)
      I.pack(pady=20,ipadx=40)
      J=Button(frame2,text='Number of Victims & Blast Day Type', command=N_V_B)
      J.pack(pady=20,ipadx=40)
      K=Button(frame2,text='Prediction', command=P_R)
      K.pack(pady=20,ipadx=40)
      M=Button(frame2,text='Binomial Distribution', command=B_D1)
      M.pack(pady=20,ipadx=40)
      fun_G.mainloop()
        
    def Exit_FUN():
      screen.clear()
      app.destroy()
      screen1 = a.Screen()
      screen1.bgcolor("cyan")
      a.color("")
      a.goto(-160,50)
      a.pensize(10)
      a.color("black")
      a.circle(75,-180)
      
      a.color("")
      a.goto(-90,190)
      a.color("black")
      a.left(90)
      a.forward(140)
      a.left(90)
      a.forward(100)
      a.color("")
      a.goto(70,60)
      a.color("black")
      a.circle(70)
      a.color("")

      a.goto(220,170)
      a.color("black")
      a.left(120)
     
      a.circle(30,250) 
     
      a.left(180)
      a.forward(10)
     
      a.circle(30,-250)
      a.color("")
      a.goto(260,180)
      a.color("black")
      a.left(60)
      a.forward(60)
      a.backward(60)
      a.right(90)
      a.forward(60)
      a.left(90)
      a.forward(60)
      a.backward(60)
      a.right(90)
      a.forward(60)
      a.left(90)
      a.forward(60)
      exit()
    frame1 = Frame(app,bg="#242424")
    frame1.pack(pady = 200,ipadx=100,ipady=150)
    
    B = Button(frame1, text ="Tabular Data", command = helloCallBack)
    C = Button(frame1, text ="Exit",command = Exit_FUN)
    ADD_Button = Button(frame1, text ="ADD",command = ADD_DATA)
    DELETE_Button = Button(frame1, text ="DELETE",command =DATA_DELETE)
    Grapic_Representation= Button(frame1, text ="Graphical Representation",command = fun_graph)
    describe= Button(frame1, text ="DesCriptive",command = fun_des)
    B.pack(pady=20,ipadx=40)
    ADD_Button.pack(pady=20,ipadx=40)
    DELETE_Button.pack(pady=20,ipadx=40)
    Grapic_Representation.pack(pady=20,ipadx=40)
    describe.pack(pady=20,ipadx=40)
    C.pack(ipadx=40)
    app.mainloop()


if __name__ == "__main__":
    screen = a.Screen()
    screen.bgcolor("cyan")
    canvas = screen.getcanvas()
    
    a.color("")
    a.goto(-100,100)
    a.pensize(10)
    a.color("black")
    a.left(0)
    a.circle(40,180)
    a.left(90)
    a.forward(150)
    a.color("")
    a.goto(-15,100)
    a.color("black")
    a.left(90)
    a.circle(40,180)
    a.left(90)
    a.forward(150)
    a.backward(70)
    a.left(45)
    a.forward(100)
    a.color("")
    a.goto(70,60)
    a.color("black")
    a.circle(70)
    a.color("")
    a.goto(220,110)
    a.color("black")
    a.left(45)
    a.circle(40,180)
    a.left(90)
    a.forward(145)
    a.left(90)
    a.circle(40,180)
    
    button = Button(canvas.master, text="START", command=do_stuff)
    canvas.create_window(80, 70, window=button)
   
    a.done()
