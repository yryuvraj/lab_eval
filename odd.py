movies = {'001': {'title': 'Inception', 'available': 3},'002': {'title': 'The Matrix', 'available': 2},
    '003': {'title': 'Interstellar', 'available': 1}}
customers = {'C1': {'name': 'Yuvraj Rathi'}, 'C2': {'name': 'Adit Garg'}}
rt = [] 

def dis():
    print("\navailable movies:")
    for movie_id, movie_info in movies.items():
        print(f"{movie_id}: {movie_info['title']} - {movie_info['available']} available")

def retmov(customer_id, movie_id):
    if customer_id not in customers:
        print(" not found.")
        return

    if movie_id in movies:
        movies[movie_id]['available'] += 1
        rt.append({'customer_id': customer_id, 'movie_id': movie_id, 'action': 'return'})
        print(f"Movie '{movies[movie_id]['title']}' returned by {customers[customer_id]['name']}.")
    else:
        print(" not found")
        
def rent(customer_id, movie_id):
    if customer_id not in customers:
        print(" not found")
        return
    
    if movie_id in movies and movies[movie_id]['available'] > 0:
        movies[movie_id]['available'] -= 1
        rt.append({'customer_id': customer_id, 'movie_id': movie_id, 'status': 'rent'})
        print(f"Movie '{movies[movie_id]['title']}' rented to {customers[customer_id]['name']}.")
    else:
        print(" not available")
        
def grr():
    print("\nRental Report:")
    for t in rt:
        customer_name = customers[t['customer_id']]['name']
        movie_title = movies[t['movie_id']]['title']
        action = t['action']
        print(f"Customer: {customer_name} | Movie: {movie_title} | Action: {action}")
    

while True:
    print("\n Movie Rental System")
    print("1.Display Available Movies")
    print("2.Rent a Movie")
    
    print("3. Return a Movie")
    print("4.Generate Rental Report")
    
    print("5.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        dis()
    elif choice == '2':
        
        customer_id = input("Enter Customer ID: ")
        movie_id = input("Enter Movie ID: ")
        rent(customer_id, movie_id)
    elif choice == '3':
        customer_id = input("Enter Customer ID: ")
        movie_id = input("Enter Movie ID: ")
        retmov(customer_id, movie_id)
    elif choice == '4':
        grr()
    elif choice == '5':
        
        break
    else:
        print("choose from 1 to 5.")
