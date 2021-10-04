#Imports
import streamlit as st
import pandas as pd
import pickle
import requests
import sqlite3
conn = sqlite3.connect('data1.db')
c = conn.cursor()


df=pd.read_csv('D:/Users/HP/Desktop/Final_Project/df_8000.csv')
similarity=pickle.load(open('D:/Users/HP/Desktop/Final_Project/similarity.pkl','rb'))


# Functions for recommendation

def get_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=6ab555c6363cd46dda63093adfffaaf3&language=en-US')
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def get_overview(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=6ab555c6363cd46dda63093adfffaaf3&language=en-US')
    data=response.json()
    return data['overview']

def get_genres(movie_id):
  A=[]
  response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=6ab555c6363cd46dda63093adfffaaf3&language=en-US')
  data=response.json()
  for i in data['genres']:
      A.append(i['name'])

  return A



def recommend(movie):
    index = df[df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    
    recommended=[]
    recommended_poster=[]
    similarity_score=[]
    recommended_overview=[]
    genre_name=[]
    for i in distances[1:11]:
        movie_id=df.iloc[i[0]].id
        #get poster
        recommended.append(df.iloc[i[0]].title)
        recommended_poster.append(get_poster(movie_id))
        similarity_score.append(i[1])
        recommended_overview.append(get_overview(movie_id))
        genre_name.append(get_genres(movie_id))
    return recommended, recommended_poster , similarity_score,recommended_overview,genre_name





# Functions for data collection
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS blogtable(userid TEXT,title TEXT,rating TEXT)')

def add_data(userid,title,rating):
	c.execute('INSERT INTO blogtable(userid,title,rating) VALUES (?,?,?)',(userid,title,rating))
	conn.commit()

def view_all_notes():
	c.execute('SELECT * FROM blogtable')
	data = c.fetchall()
	return data



#Main program

st.title('Movie Recommender')

option = st.selectbox('Select a movie ',df['title'].values)

st.write('Your Selection:', option)
ind = df[df['title'] == option].index[0]
mov=df.iloc[ind].id

######################################################################################
# Rating Section

st.subheader("Add rating ")
create_table()

userid = st.text_input("Enter User id",key='110')
rating = st.selectbox('Select rating ',('0','1','2','3','4','5'),key='101')

if st.button("Add"):
    add_data(userid,str(mov),rating)
    st.success("Thankyou {} response saved".format(userid))

results=view_all_notes()
pd.DataFrame(results).to_csv('D:/Users/HP/Desktop/Final_Project/db2_data.csv')


#######################################################################################
# Recommending Section

if st.button('Recommend Movies'):
    name , poster,score,overview,genre_list=recommend(option)
    
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.subheader(name[0])
        st.text("Silimarity\nscore:")
        st.text("%.2f" %round(score[0],2))
        st.image(poster[0])
        st.subheader("Genres")
        st.write("\n".join(genre_list[0]))
        st.subheader("Overview")
        st.write(overview[0])

    with col2:
        st.subheader(name[1])
        st.text("Silimarity\nscore:")
        st.text("%.2f" % round(score[1],2))
        st.image(poster[1])
        st.subheader("Genres")
        st.write("\n".join(genre_list[1]))
        st.subheader("Overview")
        st.write(overview[1])

    with col3:
        st.subheader(name[2])
        st.text("Silimarity\nscore:")
        st.text("%.2f" %round(score[2],2))
        st.image(poster[2])
        st.subheader("Genres")
        st.write("\n".join(genre_list[2]))
        st.subheader("Overview")
        st.write(overview[2])
        
    with col4:
        st.subheader(name[3])
        st.text("Silimarity\nscore:")
        st.text("%.2f" %round(score[3],2))
        st.image(poster[3])
        st.subheader("Genres")
        st.write("\n".join(genre_list[3]))
        st.subheader("Overview")
        st.write(overview[3])
        
    with col5:
        st.subheader(name[4])
        st.text("Silimarity\nscore:")
        st.text("%.2f" %round(score[4],2))
        st.image(poster[4])
        st.subheader("Genres")
        st.write("\n".join(genre_list[4]))
        st.subheader("Overview")
        st.write(overview[4])






    col6,col7,col8,col9,col10 = st.columns(5)
    with col6:
        st.subheader(name[5])
        st.text("Silimarity\nscore:")
        st.text("%.2f" %round(score[5],2))
        st.image(poster[5])
        st.subheader("Genres")
        st.write("\n".join(genre_list[5]))
        st.subheader("Overview")
        st.write(overview[5])

    with col7:
        st.subheader(name[6])
        st.text("Silimarity\nscore:")
        st.text("%.2f" %round(score[6],2))
        st.image(poster[6])
        st.subheader("Genres")
        st.write("\n".join(genre_list[6]))
        st.subheader("Overview")
        st.write(overview[6])

    with col8:
        st.subheader(name[7])
        st.text("Silimarity\nscore:")
        st.text("%.2f" %round(score[7],2))
        st.image(poster[7])
        st.subheader("Genres")
        st.write("\n".join(genre_list[7]))
        st.subheader("Overview")
        st.write(overview[7])

    with col9:
        st.subheader(name[8])
        st.text("Silimarity\nscore:")
        st.text("%.2f" %round(score[8],2))
        st.image(poster[8])
        st.subheader("Genres")
        st.write("\n".join(genre_list[8]))
        st.subheader("Overview")
        st.write(overview[8])

    with col10:
        st.subheader(name[9])
        st.text("Silimarity\nscore:")
        st.text("%.2f" %round(score[9],2))
        st.image(poster[9])
        st.subheader("Genres")
        st.write("\n".join(genre_list[9]))
        st.subheader("Overview")
        st.write(overview[9])        
        
        
        
