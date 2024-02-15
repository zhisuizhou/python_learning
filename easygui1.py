import easygui
#easygui.msgbox("hello")
#easygui.buttonbox("what is your color",choices = ["red","blue"])
#easygui.choicebox("what is your color",choices = ["red","blue"])
#easygui.enterbox("please input")
#easygui.integerbox("please input an integer")


a = easygui.enterbox("please input 华氏度")
b = int(a)
c = 5 / 9 * (b - 32)
c = str(c)
easygui.msgbox(c)


#C =5/9*(100-32)
