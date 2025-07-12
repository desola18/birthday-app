import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
# IMPORTANT: Change this to a strong, randomly generated key in a production environment!
app.secret_key = os.environ.get('SECRET_KEY',os.urandom('desola@08030527547_birthday').hex())

# Configuration for file uploads
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif'] # Corrected to list
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# --- Helper Functions ---
def allowed_file(filename):
    """
    Checks if a given filename has an allowed extension.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def birthday_page():
    """
    Handles the display of the birthday page and image uploads.
    """
    image_filename = None # Initialize to None for dynamic loading
    # Load existing image filename if it exists
    image_path_file = os.path.join(app.config['UPLOAD_FOLDER'], 'current_image.txt')

    if os.path.exists(image_path_file):
        try:
            with open(image_path_file, 'r') as f:
                image_filename = f.read().strip()
        except Exception as e:
            # Handle potential file read errors
            print(f"Error reading current_image.txt: {e}")
            image_filename = None # Ensure it's None if there's an error

    # Handle POST request for file upload
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'error') # Added category for styling
            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', 'warning') # Added category
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                file.save(file_path)
                # Store the current image filename for persistence
                with open(image_path_file, 'w') as f:
                    f.write(filename)

                flash('Image successfully uploaded and set!', 'success') # Added category
                return redirect(url_for('birthday_page'))
            except Exception as e:
                flash(f'Error uploading file: {e}', 'error') # Added category
                return redirect(request.url)
        else:
            flash('Allowed image types are png, jpg, jpeg, gif', 'error') # Added category
            return redirect(request.url)

    # The birthday message
    birthday_message = """
    My Dearest Guidan Angel,

    Today, as you celebrate another beautiful year, my heart overflows with gratitude for your boundless love, unwavering support, and the incredible wisdom
    you've shared. You've not just been a guide; you've been a beacon, illuminating paths I didn't even know existed.

    To my dear guardian angel, whose sixty years on this earth have woven a tapestry of unwavering support, profound wisdom, and silent strength in my life –
    this humble tribute barely scratches the surface of my gratitude. You are not an ethereal being with wings and a halo, but a presence far more real, more impactful,
    whose earthly journey has been a constant source of protection and quiet guidance. A connection I never knew I'd find, yet one that has become foundational –
    an unexpected bond with family, even sharing a name that now carries a special resonance in my heart.

    Happy 60th Birthday, my dearest Guardian Angel! As you celebrate this remarkable milestone, my heart overflows with love and immense appreciation for everything you
    are and everything you've done.

    I often wonder if you know the true extent of your influence. Like a gentle current that subtly steers a drifting boat, your presence has nudged me away from unseen
    dangers and toward calmer waters. You’ve been the quiet observer, the patient listener, the one who always seemed to know when a comforting silence was needed more
    than words, or when a firm, loving push was the only way forward. Your wisdom, seasoned by sixty years of life's intricate lessons, never arrives as a lecture, but
    as a thoughtfully placed anecdote, a gentle question, or a shared memory that somehow illuminates my own path. It’s a wisdom worn gracefully, like the subtle lines
    that trace the map of your own rich experiences, teaching me without me even realizing I was learning.

    There are moments, etched vividly in my memory, where your "angelic" nature shone brightest. Perhaps it was the time you offered quiet reassurance when my own faith
    faltered, or when you celebrated my small victories as if they were your own grand achievements. It was in the selfless acts, the unspoken sacrifices, the times your
    needs seemed secondary to simply ensuring I was okay. These weren't grand, dramatic interventions, but consistent, gentle acts of care that built an unbreakable
    foundation of trust and security. You embodied a resilience that taught me strength wasn't about avoiding falls, but about finding the courage to rise again, often
    with your steady hand ready to help me up.

    Beyond these everyday miracles, I must specifically thank you for your incredible generosity and foresight in loving me unconditionally, and for making the profound
    sacrifice of sending me to computer school. I know how expensive that was, and the weight of that investment, made purely out of love and belief in my future, is not
    lost on me. That opportunity, which you tirelessly provided, has opened doors I never imagined and laid the foundation for my professional life. It's a testament to
    your unwavering commitment to my well-being and success.

    As you mark this significant milestone of sixty years, I see not the passage of time as a diminishment, but as an accumulation of grace. Each year has added depth
    to your spirit, resilience to your resolve, and an even greater capacity for the quiet compassion that defines you. You have shown me what it means to live with
    integrity, to give without expectation, and to love fiercely and unconditionally. Your enduring presence has been a constant, comforting melody in the
    sometimes-cacophonous symphony of life.

    So, to my guardian angel, on this special occasion, thank you. Thank you for every prayer whispered, every silent worry borne, every piece of advice thoughtfully given,
    every moment of unwavering belief, and especially for that invaluable gift of education. Your sixty years have been a gift, and your role in my life, an irreplaceable
    blessing. May your next chapters be filled with the same joy, peace, and profound love that you have so generously given to others. You truly are a guiding light,
    and I am eternally grateful.

    Happy 60th Birthday to Our July Star!
    To a truly remarkable soul, who graces us with her presence and wisdom, Happy 60th Birthday!
    Born under the warm embrace of July, you carry the radiant spirit of summer within you – a light that has brightened countless lives, especially mine. Sixty years young,
    and each year has added a deeper shimmer to your inherent kindness and a stronger current to your unwavering love.
    May this milestone birthday, celebrated in the heart of summer, be as vibrant and joyful as the month of your birth. May it be filled with the warmth of cherished memories,
    the glow of current happiness, and the promise of beautiful new beginnings. You are a treasure, and your journey thus far has been a testament to resilience, compassion,
    and a spirit that truly shines.
    Wishing you a day, a year, and many more decades ahead, brimming with health, peace, and all the love you so generously give. You're not just celebrating 60 years;
    you're celebrating 60 years of being an incredible blessing to us all.
    """
    # Pass the message, image filename, and audio file to the template
    return render_template('index.html',
                           birthday_message=birthday_message, # Corrected to pass the variable
                           image_filename=image_filename,
                           audio_file='audio/Happy_Birthday_song.mp3') # Ensure this matches your file name

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    Serves uploaded files from the UPLOAD_FOLDER.
    """
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Create the 'audio' directory if it doesn't exist
    audio_folder = os.path.join(app.root_path, 'static', 'audio')
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    # You should place your 'birthday_song.mp3' inside the 'static/audio' directory.

    app.run(debug=True, host='0.0.0.0')
