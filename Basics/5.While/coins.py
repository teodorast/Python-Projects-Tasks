coins_amount = float(input())
stotinki = int(coins_amount*100)
coins_count = 0


while stotinki > 0:
    if stotinki>=200:
        stotinki -=200

    elif stotinki>=100:
        stotinki -=100

    elif stotinki>=50:
        stotinki -=50

    elif stotinki>=20:
        stotinki -=20
  
    elif stotinki>=10:
        stotinki -=10
   
    elif stotinki>=5:
        stotinki -=5
      
    elif stotinki>=2:
        stotinki -=2

    elif stotinki>=1:
        stotinki -=1
             
    coins_count+=1

    
print(coins_count)
