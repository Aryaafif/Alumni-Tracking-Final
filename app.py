from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required

app = Flask(__name__)
app.secret_key = 'kunci_rahasia_arya'

# Konfigurasi Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id): self.id = id

@login_manager.user_loader
def load_user(user_id): return User(user_id)

@app.route('/')
def index(): return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'alumni2026':
            login_user(User(id=1))
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    # Simulasi Data Berdasarkan Daily 4 (142.292 total data)
    total_data_awal = 142292
    data_ditemukan = 61185  # Misal hasil penelusuran poin 1-8
    
    # Rumus Nilai Coverage = (Ditemukan / Total) * 100
    coverage_score = round((data_ditemukan / total_data_awal) * 100)
    
    # Data Alumni Hasil Penelusuran (Poin 1-8)
    alumni_list = [
        {
            "nama": "Catur Rahmani Oktavia",
            "nim": "95620625",
            "sosmed": "LI: catur-o, IG: @catur_okta",
            "email": "catur@mail.com",
            "hp": "08123456789",
            "kantor": "PT. Bakti Jaya",
            "alamat_kantor": "Jakarta Selatan",
            "posisi": "Finance Manager",
            "kategori": "Swasta",
            "sosmed_kantor": "IG: @baktijaya_id"
        },
        # Tambahkan data lainnya sesuai list yang kamu punya
    ]
    
    return render_template('dashboard.html', 
                           alumni=alumni_list, 
                           total=total_data_awal, 
                           found=data_ditemukan, 
                           cvg=coverage_score)

if __name__ == '__main__':
    app.run(debug=True)