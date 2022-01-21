size(500,500)

background(random(50),random(50),random(50))

fill(random(150,500),random(150,500),random(150,500))
noStroke()

x = random(100,200)

rect(x, 350, random(100,300),100)
xb = x+random(100)
rect(xb, 250,random(100,200),100)
xc = x+random(100)
rect(xc, 150, random(100),100)

fill(random(100,150),random(100,150),random(100,150))

rect(x-20, 350, random(100,300),100)
rect(xb-50, 250,random(100,200),100)
rect(xc-20, 150, random(100),100)
