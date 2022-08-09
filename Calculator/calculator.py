
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_file('.//calculator_by_pranav.kv')
Window.size=(350,550)
counter=0
class Calculator_by_PranavWidget(Widget):

    def clear(self):
        self.ids.input_box.text='0'

    def button_value(self, number):
        global counter

        prev_num=self.ids.input_box.text

        if self.ids.input_box.text=='0' or self.ids.input_box.text=='ERROR' :
            counter=0
            self.ids.input_box.text=''
            self.ids.input_box.text=f"{number}"
        elif self.ids.input_box.text!='0':
            self.ids.input_box.text= f"{self.ids.input_box.text}{number}"

    def backspace(self):
        prev_num=self.ids.input_box.text
        prev_num=prev_num[:-1]
        self.ids.input_box.text=f"{prev_num}"

    def sign(self,sign):
        prev_num=self.ids.input_box.text
        if prev_num=="ERROR":
            self.ids.input_box.text=f"0"

        prev_num=prev_num[-1:]
        if prev_num=='+' or prev_num=='-' or prev_num=='/' or prev_num=='x' or prev_num=='%':
            prev_num=self.ids.input_box.text
            prev_num=prev_num[:-1]
            self.ids.input_box.text=f"{prev_num}{sign}"
            
        else:
            self.ids.input_box.text=f"{self.ids.input_box.text}{sign}"

    def decimal(self):
        prev_num=self.ids.input_box.text
        prev_num=prev_num[-1:]
        try:
            prev_num=int(prev_num)
            self.ids.input_box.text=f"{self.ids.input_box.text}."

        except:
            pass    

    def calculation(self):
        global counter
        counter=1
        string=  self.ids.input_box.text
        try:

            nums=re.split('[+]|[-]|[x]|[/]',string)
            
            nums=list(map(float,nums))
                
            signs=re.findall('[+]|[-]|[x]|[/]',string)

            n=0 
            while n<len(signs):
                if signs[n]=="/":
                    temp=nums[n]/nums[n+1]
                    nums.pop(n)
                    nums.pop(n)
                    nums.insert(n,temp)
                    signs.pop(n)
                n=n+1  
                
            n=0 
            while n<len(signs):
                if signs[n]=="x":
                    temp=nums[n]*nums[n+1]
                    nums.pop(n)
                    nums.pop(n)
                    nums.insert(n,temp)
                    signs.pop(n)
                n=n+1        
                
            n=0 
            while n<len(signs):
                if signs[n]=="+":
                    temp=nums[n]+nums[n+1]
                    nums.pop(n)
                    nums.pop(n)
                    nums.insert(n,temp)
                    signs.pop(n)
                n=n+1   
                
            n=0 
            while n<len(signs):
                if signs[n]=="-":
                    temp=nums[n]-nums[n+1]
                    nums.pop(n)
                    nums.pop(n)
                    nums.insert(n,temp)
                    signs.pop(n)
                n=n+1       
                    
            print(nums[0])  
            ans=str(nums[0])
            # if len(ans)>13:
            #     a=len(ans)-13
            #     ans=ans[:-a]
            try:  
                if float(nums[0])==int(nums[0]):
                    ans=int(nums[0])
            except: 
                pass           
            self.ids.input_box.text=f"{ans}"


        except:
            self.ids.input_box.text=f"ERROR"




class Calculator_by_PranavApp(App):
    def build(self):
        return Calculator_by_PranavWidget()

if __name__=="__main__":
    Calculator_by_PranavApp().run()
