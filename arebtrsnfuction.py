def test(a,b,c,*d,**e):
    print("a:",a,"b:",b,"c:",c,"d:",d,"E:",e)

test(1,2,3,4,5,6,7,x=10,y=20,z=30)    
