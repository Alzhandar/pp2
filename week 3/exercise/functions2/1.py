l = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
l1=[]
#1
for i in l: 
    l1.append(i["imdb"])
for i in l1:
    if i>5.5:
        print("True")
    else:
        print("False")
#2
for i in l:
    if i["imdb"]>5.5:
        print(i["name"])
#3
a=input()
for i in l:
    if i["category"]==a:
        print(i["name"])
#4        
sum=0
for i in l:
    sum+=i["imdb"]
print(sum/len(l))
#5
rez=0
s=input()
for i in l:
    if i["category"]==a:
        rez+=i["imdb"]
print(rez)
