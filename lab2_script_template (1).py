def main():

    # TODO: Step 2 - Create a complex data structure
    about_me =  {'Full_name':'luckson paija',
                'student_id':'10310712',
                'Pizza_toppings':[
                    'PEPERONI',
                    'CHEESE',
                    'PINEAPPLE'
                ],
                'movies': [
                    { 'title':'The Wolf of the wall street',
                    'genre':'crime' },
                    { 'title':'Fast and Furious',
                    'genre':'Action' }
                    
                    
                ]
                }

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title':'Big Hero 6','genre':'animation'})
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name =about_me['Full_name']
    first_name =full_name.split()[0]
    student_id=about_me["student_id"]
    print(f"My name is {full_name},but you can call me sir {first_name}.")
    print(f"My student ID is {student_id}.")
    print_student_name_and_id(about_me)
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me,toppings):
        return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    for topping in about_me:
        if about_me[topping]:
            print(f"{topping}")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
  movie_genres =  return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
            titles=[movie['title'].title() for movie in movie_list]
            print("Some of my  favorite movies are")     
            for title in enumerate(titles):
                print(f"{title}")          
            
            return
    
if __name__ == '__main__':
    main()