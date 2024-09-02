from django.shortcuts import render
from datetime import date

all_posts = [
    {
    "slug" : "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Trivi",
    "date": date(2021,7,21),
    "title":"The Mountains",
    "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima consequatur delectus ad quos amet veritatis fugiat! Ex, harum odit sit consequuntur repudiandae laborum eaque beatae eum unde dolorum minima repellendus.",
    "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima consequatur delectus ad quos amet veritatis fugiat! Ex, harum odit sit consequuntur repudiandae laborum eaque beatae eum unde dolorum minima repellendus.
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima consequatur delectus ad quos amet veritatis fugiat! Ex, harum odit sit consequuntur repudiandae laborum eaque beatae eum unde dolorum minima repellendus.
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima consequatur delectus ad quos amet veritatis fugiat! Ex, harum odit sit consequuntur repudiandae laborum eaque beatae eum unde dolorum minima repellendus.
    """,
    },

    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },

    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post['date']
# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts" : latest_posts,
    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts" : all_posts,
    })

def post_detail(request,slug):
    try:
        identified_post =next(post for post in all_posts if post['slug'] == slug)
        return render(request,"blog/post-detail.html",{
        "post":identified_post,
    })

    except:
        return render(request,'404.html')