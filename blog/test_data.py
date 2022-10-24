from .models import Blog, CATEGORIES
from account.models import User
import requests
import random
from django.shortcuts import HttpResponse


def save_image():
    url = 'https://picsum.photos/200/200'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        response.raw.decode_content = True
        # save it to local
        random_name = f"image-{random.randint(1, 1000000)}.jpg"
        with open(f"static/test/{random_name}", 'wb') as f:
            f.write(response.content)

        return f"static/test/{random_name}"
    else:
        return None

LOREM_IPSUM_SUMMARY = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia, \
molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum \
numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium \
optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis \
obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam \
nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,"""

LOREM_IPSUM_CONTENT = """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia, \
molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum \
numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium \
optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis \
obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam \
nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,"
Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia, \
molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum \
numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium \
optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis \
obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam \
nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,"
Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia, \
molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum \
numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium \
optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis \
obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam \
nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,"""

def create_blog(request):
    try:
        password = request.GET.get('password')
        if password != 'strongpassword1234':
            return HttpResponse('Wrong password')
    except:
        return HttpResponse('Wrong password')
    user = User.objects.get(username="demo_doctor")
    for i in range(20):
        blog = Blog.objects.create(
            title=f"Blog {i}",
            summary=LOREM_IPSUM_SUMMARY,
            content=LOREM_IPSUM_CONTENT,
            category=random.choice(CATEGORIES),
            author=user,
            is_draft = random.choice([True, False]),
            image=save_image(),
        )
        blog.save()
        print(f"Blog {blog} created")

    return HttpResponse(f"""
    <h1>20 Blog created</h1>
    <a href="/">Home</a>
    """)

