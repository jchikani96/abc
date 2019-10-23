import tkinter as tk
import requests

def test_function(entry):
	print("This is a Entry: ",entry)

def format_response(weather):
	try:
		name=weather['name']
		desc=weather['weather'][0]['description']
		temp=weather['main']['temp']

		final_str='City:%s\nCondition:%s\nTempreture:%s' %(name,desc,temp)

	#return str(name)+' ' +str(desc)+' ' +str(temp)
	except:
		final_str='there was a problem'

	return final_str



def get_weather(city):
	weather_key='df24e2266345d25242b859d5f71cf4b1'
	url='https://api.openweathermap.org/data/2.5/weather'
	params={'APPID':weather_key,'q':city,'units':'Metric'}
	response=requests.get(url,params=params)
#	print(response.json())
	weather=response.json()
	label['text'] = format_response(weather)
 

	
HEIGHT=500
WIDTH=600

root=tk.Tk()
# df24e2266345d25242b859d5f71cf4b1
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image=tk.PhotoImage(file='smoke-png-images-download-10525-png-resources-with-transparent-pictures-of-png-650_1155.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame=tk.Frame(root,bg='powder blue',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.78,relheight=0.1,anchor='n')

entry=tk.Entry(frame,text="Enter your name of city",font=40)
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text="Get Button",font=40,command=lambda:get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)
#button.grid(row=0,column=1)

lower_frame=tk.Frame(root,bg='#80c1ff',bd=9)
lower_frame.place(relx=0.5,rely=0.25,relheight=0.75,relwidth=0.75,anchor='n')

label=tk.Label(lower_frame,bg="yellow",font=('arial',20),anchor='nw',justify='left')
label.place(relwidth=1,relheight=1)



root.mainloop()