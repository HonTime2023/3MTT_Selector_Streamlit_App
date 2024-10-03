import streamlit as st

def display_items(selected_items):
    # Add CSS for styling
    st.markdown(
        """
        <style>
            .item-name {
                color: black;  /* Set text color to black */
                font-size: 24px;  /* Set font size */
                margin: 0;  /* Remove margin */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    for item in selected_items:
        st.markdown(
            f"""
            <div style="
                display: flex;
                justify-content: space-between;
                align-items: center;
                border: 2px solid #4CAF50;
                border-radius: 15px;
                padding: 10px;
                margin-bottom: 20px;
                background-color: #f9f9f9;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            ">
                <div style="flex: 1;">
                    <img src="{item['image']}" style="width: 150px; height: auto; border-radius: 10px;" />
                </div>
                <div style="flex: 2; text-align: right; padding-left: 20px;">
                    <h2 class="item-name">{item['name']}</h2>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# Start the Streamlit app
def streamlit_app():
    st.title('Item Selector')

    # Define 7 lists of related items
    fruits = [
        {"name": "Apple", "image": "https://th.bing.com/th/id/R.9c4d8dc9fb6e499ae567a455c6d9abcc?rik=xJzuU5VsKl%2bN8w&riu=http%3a%2f%2fclipart-library.com%2fimages_k%2ftransparent-apple%2ftransparent-apple-21.png&ehk=0LDP56MKEPdTs%2bGgu%2fBTfq2yqFWK9CympqcCzj7GOs4%3d&risl=&pid=ImgRaw&r=0"},
        {"name": "Banana", "image": "https://th.bing.com/th/id/R.b68ce613e38948927ff9f3fadba634b7?rik=LDx5P6%2bvdgJd9Q&riu=http%3a%2f%2fpngimg.com%2fuploads%2fbanana%2fbanana_PNG825.png&ehk=FerCPHBthVSqhdMcgR1ivW%2fR7NnStJdUbms1nFl1cIM%3d&risl=&pid=ImgRaw&r=0"},
        {"name": "Orange", "image": "https://th.bing.com/th/id/OIP.fU1OBf6zpJvfSZ0HMOqudQHaHy?rs=1&pid=ImgDetMain"},
        {"name": "Grapes", "image": "https://th.bing.com/th/id/OIP.lk121VKGCkF3Xe3UogIq8AHaHM?rs=1&pid=ImgDetMain"},
        {"name": "Strawberry", "image": "https://th.bing.com/th/id/R.6b3e5b5c7b8db887e7775c3dd85409d4?rik=Yyf479uQzWLTSA&pid=ImgRaw&r=0"}
    ]

    cars = [
        {"name": "Tesla Model S", "image": "https://th.bing.com/th/id/R.0a3dd2113dd779ff889514bc8b784fb5?rik=hxOA022D8%2bjwAQ&pid=ImgRaw&r=0"},
        {"name": "BMW 3 Series", "image": "https://th.bing.com/th/id/R.860eb54f11dca34121c83202c6da05fe?rik=vYn92D2xzV9UTA&riu=http%3a%2f%2fclipart-library.com%2fimages_k%2fbmw-transparent%2fbmw-transparent-3.png&ehk=Vz3I2bKG52TxdhWRwY2dRYeiNU9gY8xSZ9fz4qT4uN0%3d&risl=&pid=ImgRaw&r=0"},
        {"name": "Audi A4", "image": "https://th.bing.com/th/id/R.ed9798b70c6813eecd1cd233d93dccb2?rik=w72r8iWC%2baHd3Q&pid=ImgRaw&r=0"},
        {"name": "Mercedes-Benz C-Class", "image": "https://th.bing.com/th/id/R.b6517a96d21d364809305bb5bfaf2f46?rik=9C8FyP264ggfCQ&pid=ImgRaw&r=0"},
        {"name": "Lamborghini", "image": "https://th.bing.com/th/id/R.4ab841533eb8e379402dead3fb0c149e?rik=RSPIj0VhU6j%2bJA&pid=ImgRaw&r=0"}
    ]

    programming_languages = [
        {"name": "Python", "image": "https://pluspng.com/img-png/python-logo-png-open-2000.png"},
        {"name": "JavaScript", "image": "https://pluspng.com/img-png/logo-javascript-png-alternate-image-for-javascript-480.png"},
        {"name": "Java", "image": "https://brandlogos.net/wp-content/uploads/2021/11/java-logo.png"},
        {"name": "C++", "image": "https://clipart-library.com/image_gallery2/C-PNG-Clipart.png"},
        {"name": "Ruby", "image": "https://1.bp.blogspot.com/-67bM1TvpHqU/V_Pi46iq7FI/AAAAAAAAAh8/Euxl6HD5NFYUwyOi2DVKVM1pbqlH8gj0wCLcB/s1600/1000px-Ruby-logo-R.svg.png"}
    ]

    animals = [
        {"name": "Lion", "image": "https://pluspng.com/img-png/lion-hd-png--1850.png"},
        {"name": "Elephant", "image": "https://th.bing.com/th/id/R.e54c93fffe98a3cb472ff34c80621f59?rik=rnh1vV0iEgxzHg&pid=ImgRaw&r=0&sres=1&sresct=1"},
        {"name": "Tiger", "image": "https://th.bing.com/th/id/R.52de9124c03a022794152af9d3f59e20?rik=%2b%2bgypUC1FYZzJA&riu=http%3a%2f%2fpluspng.com%2fimg-png%2ftiger-hd-png-tiger-png-pictures-image-39177-png-tiger-face-2560.png&ehk=g7At2CDvx1%2fNviU4vaO25mqx1FwtEF%2fTuZoXZ0cNlyg%3d&risl=&pid=ImgRaw&r=0"},
        {"name": "Giraffe", "image": "https://th.bing.com/th/id/R.31288a8355b3be8f213cdd2f0331c818?rik=DhgMW8RC67HAKw&riu=http%3a%2f%2fpluspng.com%2fimg-png%2fpng-hd-giraffe-giraffe-png-1020.png&ehk=JU%2b3wBq%2bPs5h0qPwWyFm%2bd1vSq61ln%2fUebsQwmBfsEI%3d&risl=&pid=ImgRaw&r=0"},
        {"name": "Zebra", "image": "https://th.bing.com/th/id/R.90f9c4f8cde21b509a5523670f21902c?rik=vYaYeiwsGQ3zZA&riu=http%3a%2f%2fpluspng.com%2fimg-png%2fzebra-hd-png-zebra-resimleri-874.png&ehk=s8%2fw3R4zl6jrnBeEhLSghF5IdbL3Twg5vWPuEIpdvQg%3d&risl=&pid=ImgRaw&r=0"}
    ]

    ocean_animals = [
        {"name": "Dolphin", "image": "https://th.bing.com/th/id/R.3259db3825b3fcd3abb33ac1ee1eb52a?rik=tbagZkKnqw%2bvNA&riu=http%3a%2f%2fpluspng.com%2fimg-png%2fdolphin-hd-png--968.png&ehk=1YLgdYfmZh7bhTt0wpcp0%2bETPsqn3MLUIXItDsJQ0WU%3d&risl=&pid=ImgRaw&r=0"},
        {"name": "Whale", "image": "https://th.bing.com/th/id/R.2b308dad834e54d816275a9223c6cb82?rik=5XomQGwEDDugIw&pid=ImgRaw&r=0"},
        {"name": "Shark", "image": "https://th.bing.com/th/id/R.cd9eec9f2b20eafd343158b1b014debf?rik=MAfBRHb5hQIsOA&pid=ImgRaw&r=0"},
        {"name": "Octopus", "image": "https://th.bing.com/th/id/R.ec162d459ead82c9a926b61d72a8df9d?rik=bgscor%2bH0p4Rxw&pid=ImgRaw&r=0"},
        {"name": "Sea Turtle", "image": "https://th.bing.com/th/id/R.b44a535fa540ec4237efe2b867882b6a?rik=2b9uFZm7KDCIbw&pid=ImgRaw&r=0"}
    ]

    # Combine all lists
    all_items = {
        'Fruits': fruits,
        'Cars': cars,
        'Programming Languages': programming_languages,
        'Animals': animals,
        'Ocean Animals': ocean_animals
    }

    # Sidebar for category selection
    selected_category = st.sidebar.selectbox('Select Category', list(all_items.keys()))

    # Sidebar for item selection
    selected_items = []
    st.sidebar.title(f"Select Items from {selected_category}")
    for item in all_items[selected_category]:
        if st.sidebar.checkbox(item['name']):
            selected_items.append(item)

    # Display the selected items
    if selected_items:
        st.subheader(f'Selected Items from {selected_category}:')
        display_items(selected_items)
    else:
        st.write("No items selected.")


# Run the app
if __name__ == '__main__':
    streamlit_app()