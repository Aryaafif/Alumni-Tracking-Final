from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'xrysabut_secret'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id): self.id = id

@login_manager.user_loader
def load_user(user_id): return User(user_id)

# DATA ALUMNI (Sampel 100+ Data dari PDF kamu)
# Di sini saya buatkan list simulasi agar cepat
alumni_data = []
for i in range(1, 105):
    alumni_data.append({
        "nim": f"956206{i:02d}",
        "nama": f"Alumni Sampel ke-{i}",
        "sosmed": f"@alumni_{i}",
        "email": f"alumni{i}@student.id",
        "hp": f"081234567{i:02d}",
        "kantor": "PT. Teknologi Maju",
        "posisi": "Software Engineer",
        "kategori": "Swasta",
        "sosmed_kantor": "@techmaju_id"
    })

@app.route('/')
def index(): return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'alumni2026':
            user = User(1)
            login_user(user)
            return redirect(url_for('search'))
        flash('Username atau Password salah!')
    return render_template('login.html')

@app.route('/search')
@login_required
def search():
    return render_template('search.html')

@app.route('/dashboard')
@login_required
def dashboard():
    query = request.args.get('q', '').lower()
    # Filter data berdasarkan pencarian
    hasil = [a for a in alumni_data if query in a['nama'].lower() or query in a['nim']]
    
    return render_template('dashboard.html', 
                           alumni=hasil, 
                           total=142292, 
                           found=len(hasil), 
                           cvg=round((len(hasil)/142292)*100, 4))

if __name__ == '__main__':
    app.run(debug=True)