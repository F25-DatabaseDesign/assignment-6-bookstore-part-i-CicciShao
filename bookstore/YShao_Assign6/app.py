from flask import Flask, render_template, request

app = Flask(__name__)

# ====================
# 1. Categories (dicts)
# ====================
categories = [
    {"id": 1, "name": "Cozy Romance", "image": "category_1.png"},
    {"id": 2, "name": "Fantasy", "image": "category_2.png"},
    {"id": 3, "name": "Classics", "image": "category_3.png"},
    {"id": 4, "name": "Children's Books", "image": "category_4.png"}
]


# ====================
# 2. Books (dicts)
# ====================
books = [
    {
        "id": 1,
        "categoryId": 1,
        "title": "The Café on Maple Street",
        "author": "Emily Hart",
        "isbn": "9780143120000",
        "price": 12.99,
        "image": "cozy_romance_1.png",
        "readNow": 1
    },
    {
        "id": 2,
        "categoryId": 1,
        "title": "Autumn Letters",
        "author": "Sophie Brooks",
        "isbn": "9780525510000",
        "price": 10.50,
        "image": "cozy_romance_2.png",
        "readNow": 0
    },
    {
        "id": 3,
        "categoryId": 1,
        "title": "Warm Nights in Paris",
        "author": "Clara Bennett",
        "isbn": "9781501120000",
        "price": 13.75,
        "image": "cozy_romance_3.png",
        "readNow": 1
    },
    {
        "id": 4,
        "categoryId": 1,
        "title": "Sunlit Afternoons",
        "author": "Hannah Wells",
        "isbn": "9780062800000",
        "price": 11.20,
        "image": "cozy_romance_4.png",
        "readNow": 0
    },

    # Fantasy
    {
        "id": 5,
        "categoryId": 2,
        "title": "The Moonlight Keeper",
        "author": "Aiden Frost",
        "isbn": "9780593300000",
        "price": 14.99,
        "image": "fantasy_1.png",
        "readNow": 1
    },
    {
        "id": 6,
        "categoryId": 2,
        "title": "Wings of the Evergreen",
        "author": "Lyra Dawn",
        "isbn": "9780316200000",
        "price": 12.25,
        "image": "fantasy_2.png",
        "readNow": 0
    },
    {
        "id": 7,
        "categoryId": 2,
        "title": "The Enchanted Lantern",
        "author": "Marion Vale",
        "isbn": "9781473210000",
        "price": 15.50,
        "image": "fantasy_3.png",
        "readNow": 1
    },
    {
        "id": 8,
        "categoryId": 2,
        "title": "Forest of Whispers",
        "author": "Serena Moss",
        "isbn": "9781250800000",
        "price": 13.40,
        "image": "fantasy_4.png",
        "readNow": 0
    },

    # Classics
    {
        "id": 9,
        "categoryId": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "isbn": "9780141439518",
        "price": 9.99,
        "image": "classics_1.png",
        "readNow": 1
    },
    {
        "id": 10,
        "categoryId": 3,
        "title": "Little Women",
        "author": "Louisa May Alcott",
        "isbn": "9780147514011",
        "price": 8.99,
        "image": "classics_2.png",
        "readNow": 0
    },
    {
        "id": 11,
        "categoryId": 3,
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "isbn": "9780141441146",
        "price": 10.50,
        "image": "classics_3.png",
        "readNow": 1
    },
    {
        "id": 12,
        "categoryId": 3,
        "title": "Anne of Green Gables",
        "author": "L.M. Montgomery",
        "isbn": "9781402288944",
        "price": 7.95,
        "image": "classics_4.png",
        "readNow": 0
    },

    # Children's Books
    {
        "id": 13,
        "categoryId": 4,
        "title": "The Wishful Woods",
        "author": "Olivia Starling",
        "isbn": "9780593400000",
        "price": 8.50,
        "image": "kids_1.png",
        "readNow": 1
    },
    {
        "id": 14,
        "categoryId": 4,
        "title": "Bunny’s Big Adventure",
        "author": "Rosie Turner",
        "isbn": "9781524760000",
        "price": 7.10,
        "image": "kids_2.png",
        "readNow": 0
    },
    {
        "id": 15,
        "categoryId": 4,
        "title": "The Secret Treehouse",
        "author": "Ben Carter",
        "isbn": "9780062490000",
        "price": 8.25,
        "image": "kids_3.png",
        "readNow": 1
    },
    {
        "id": 16,
        "categoryId": 4,
        "title": "Cloudberry Dreams",
        "author": "Ella Winter",
        "isbn": "9780375830000",
        "price": 6.99,
        "image": "kids_4.png",
        "readNow": 0
    }
]

# ====================
# 3. Routes
# ====================

@app.route('/')
def home():
    return render_template("index.html", categories=categories)


@app.route('/category')
def category():
    # Read category ID from URL
    cat_id = request.args.get("cat")
    if not cat_id:
        return render_template("error.html", error="Missing category.")
    cat_id = int(cat_id)

    # Filter selected category
    selected_category = next((c for c in categories if c["id"] == cat_id), None)
    if not selected_category:
        return render_template("error.html", error="Invalid category.")

    # Filter books in that category
    selected_books = [b for b in books if b["categoryId"] == cat_id]

    return render_template(
        "categories.html",
        categories=categories,
        categoryId=cat_id,
        books=selected_books
    )


# @app.route('/search')
# def search():
#     return render_template("search.html")


@app.errorhandler(Exception)
def handle_error(e):
    import traceback
    print("=== ERROR ===")
    traceback.print_exc()   # 打印真正错误
    return render_template("error.html", error=str(e))



if __name__ == "__main__":
    app.run(debug=True)

