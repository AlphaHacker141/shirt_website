import sqlite3
import random

DB_NAME = 'database.db'

products = [
    ("Urban Legend", "Oversized", "The ultimate streetwear essential."),
    ("Night Crawler", "Anime", "Glow in the dark anime print."),
    ("Neon Demon", "Typography", "Bold neon typography for the bold you."),
    ("Tokyo Drift", "Anime", "Inspired by the streets of Tokyo."),
    ("Gym Beast", "Gym", "Unleash the beast within."),
    ("Minimalist Vibe", "Minimalist", "Less is more. Premium cotton."),
    ("Abstract Art", "Typography", "Wearable art for the creative soul."),
    ("Retro Wave", "Bollywood", "Bringing back the 90s bollywood vibe."),
    ("Cyber Punk", "Anime", "Future is now."),
    ("Street King", "Oversized", "Rule the streets with this fit."),
    ("Oversized Basic", "Minimalist", "Your everyday go-to oversized tee."),
    ("Anime Hero", "Anime", "For the otaku in you."),
    ("Gamer Life", "Typography", "Level up your style."),
    ("Code Master", "Typography", "Eat. Sleep. Code. Repeat."),
    ("Future Tech", "Minimalist", "Sleek design for the modern era."),
    ("Vintage Soul", "Bollywood", "Classic never goes out of style."),
    ("Nature Lover", "Minimalist", "Organic cotton, earth friendly."),
    ("Space Cadet", "Anime", "To the moon and beyond."),
    ("Music Junkie", "Typography", "Feel the beat."),
    ("Artistic Chaos", "Oversized", "Embrace the chaos.")
]

images = ['shirt1.jpg', 'shirt2.jpg', 'shirt3.jpg', 'shirt4.jpg']

def seed_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Clear existing products
    cursor.execute('DELETE FROM products')
    
    for name, category, desc in products:
        price = random.choice([499, 599, 699, 799, 899, 999])
        image = random.choice(images)
        
        cursor.execute('''
            INSERT INTO products (name, price, image_filename, category, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, price, image, category, desc))
        
    conn.commit()
    conn.close()
    print("Database seeded with 20 products!")

if __name__ == '__main__':
    seed_db()
