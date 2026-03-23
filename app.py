from flask import Flask, jsonify
import os

app = Flask(__name__)

# Public index page HTML
INDEX_HTML = '''<!DOCTYPE html><html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Oldbridge Media</title>
  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <style>
    :root {
      --navy: #001f3f;
      --gold: #FFD700;
      --bg-dark: #001b35;
      --text-light: #f5f5f5;
    }
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background: var(--navy);
      color: var(--text-light);
    }
    header {
      text-align: center;
      padding: 30px 15px 10px;
    }
    header img {
      width: 500px;
      max-width: 95%;
      border-radius: 10px;
    }
    header h1 {
      color: var(--gold);
      font-size: 34px;
    }
    .social-icons a {
      font-size: 24px;
      color: var(--gold);
      margin: 0 10px;
      text-decoration: none;
    }
    section {
      background: var(--bg-dark);
      padding: 30px 20px;
      max-width: 1000px;
      margin: 20px auto;
      border-radius: 10px;
    }
    h2 { color: var(--gold); }
    .service-box, .team-box {
      background: var(--navy);
      border-left: 5px solid var(--gold);
      border-radius: 10px;
      padding: 15px;
      margin-bottom: 15px;
    }
    footer {
      background: var(--navy);
      text-align: center;
      padding: 15px;
      color: var(--gold);
    }
  </style>
</head>
<body><header>
  <img src="https://i.postimg.cc/7L89B29P/IMG-20250608-WA0014.jpg" alt="Oldbridge Media Logo" />
  <h1>Oldbridge Media</h1>
  <p><em>Bridging Stories. Honoring Roots. Shaping Futures.</em></p>
  <div class="social-icons">
    <a href="#"><i class="fab fa-facebook"></i></a>
    <a href="#"><i class="fab fa-instagram"></i></a>
    <a href="mailto:info@oldbridgemedia.com"><i class="fas fa-envelope"></i></a>
  </div>
</header><section>
  <h2>🎯 Our Identity</h2>
  <div class="service-box"><strong>Mission:</strong> To produce authentic, African-rooted stories that empower, educate, and entertain.</div>
  <div class="service-box"><strong>Vision:</strong> To become a Pan-African creative powerhouse revolutionizing media content.</div>
  <div class="service-box"><strong>Objectives:</strong> Build community, empower creators, expand digital presence, and partner globally.</div>
  <div class="service-box"><strong>Core Values:</strong> Integrity, Excellence, Ubuntu, Creativity, Representation.</div>
</section><section>
  <h2>🎨 Creative Philosophy</h2>
  <p><em>"We believe the best African stories are told by Africans. We craft from the inside out, not from an outsider's gaze."</em></p>
</section><section>
  <h2>👥 Our Team</h2>
  <div class="team-box">
    <strong>Lorato Tembwe</strong> – Founder & Director<br/>
    Supported by a passionate creative crew, freelancers, and community collaborators.
  </div>
</section><section>
  <h2>🎯 Target Audience</h2>
  <p>TV Networks, NGOs, Event Planners, Academics, and Cultural Institutions across Africa.</p>
</section><section>
  <h2>💼 Revenue Streams</h2>
  <ul>
    <li>Film & TV Commissions</li>
    <li>Live & Virtual Event Production</li>
    <li>Film Equipment Rentals</li>
    <li>Content Licensing & Distribution</li>
    <li>Training & Creative Workshops</li>
  </ul>
</section><section>
  <h2>🏆 Achievements & Future Goals</h2>
  <p>We've produced acclaimed short films, partnered with festivals, and aim to launch our own Oldbridge Film Festival. We're working towards streaming on Netflix, Showmax, and more.</p>
</section><section>
  <h2>📡 Our Services</h2>
  <div class="service-box">
    <h3>🎬 Film & TV Productions</h3>
    <p>From concept to screen, Oldbridge Media delivers cinematic content—scripting, directing, shooting, and editing under one roof.</p>
  </div>
  <div class="service-box">
    <h3>📡 Live Streaming</h3>
    <p>Seamless, high-definition streaming for conferences, concerts, weddings, and hybrid experiences.</p>
  </div>
  <div class="service-box">
    <h3>🎉 Event Coverage</h3>
    <p>Capture your most important moments with expert photography, videography, and editing services.</p>
  </div>
  <div class="service-box">
    <h3>🎥 Film Equipment Hire</h3>
    <p>Rent industry-grade cameras, audio gear, and lighting setups—ideal for indie shoots and professional productions.</p>
  </div>
</section><section>
  <h2>📍 Contact & About</h2>
  <p>Founded in 2024 by <strong>Lorato Tembwe</strong>, Oldbridge Media is a Botswana-based TV and media production company inspired by African traditions. Our mission is to blend heritage and modern storytelling to shape the continent's future narratives.</p>
  <p><strong>Address:</strong> Boseja Route 9, Plot 3829, Maun</p>
  <p><strong>Contact:</strong> +267 74808932</p>
  <p><strong>Email:</strong> <a href="mailto:info@oldbridgemedia.com">info@oldbridgemedia.com</a></p>
</section><footer>
  &copy; 2025 Oldbridge Media. All rights reserved.
<div class="social-icons" style="margin-top: 10px;">
    <a href="https://facebook.com" target="_blank"><i class="fab fa-facebook"></i></a>
    <a href="https://instagram.com" target="_blank"><i class="fab fa-instagram"></i></a>
    <a href="mailto:info@oldbridgemedia.com"><i class="fas fa-envelope"></i></a>
</div>

<section id="announcements" style="padding: 30px; background: #f8f8f8;">
  <h2 style="color: #001f3f; text-align:center;">📢 Latest Announcements</h2>
  <div id="posts" style="max-width: 800px; margin: auto;"></div>
</section>
<script>
  fetch("https://old-bridge-backend.onrender.com/api/posts")
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("posts");
      if (!data.posts.length) {
        container.innerHTML = "<p style='text-align:center;'>No announcements yet.</p>";
        return;
      }
      data.posts.reverse().forEach(post => {
        const html = `
          <div style='background:#fff; margin:20px 0; padding:15px; border-left:5px solid gold; border-radius:6px; box-shadow:0 0 8px rgba(0,0,0,0.1);'>
            <h3 style='color:#001f3f;'>${post.title}</h3>
            <p>${post.message}</p>
            ${post.image ? `<img src="https://old-bridge-backend.onrender.com${post.image}" style="max-width:100%; margin-top:10px; border-radius:6px;" />` : ''}
          </div>
        `;
        container.innerHTML += html;
      });
    })
    .catch(err => console.error("Error loading posts:", err));
</script>
</footer>
</body>
</html>'''

# Admin panel HTML
ADMIN_HTML = '''<!DOCTYPE html>
<html>
<head>
  <title>[ADMIN] Oldbridge Media Admin Panel</title>
  <style>
    body { font-family: Arial, sans-serif; background: #001f3f; color: white; padding: 20px; }
    input, textarea, button {
      display: block;
      width: 100%;
      margin: 10px 0;
      padding: 10px;
      border: none;
      border-radius: 5px;
      box-sizing: border-box;
    }
    input[type="file"] { background: white; color: black; }
    .post {
      background: #002f5f;
      padding: 15px;
      margin-bottom: 10px;
      border-left: 5px solid gold;
      border-radius: 5px;
    }
    h1, h2 { color: gold; }
    .delete-btn {
      background: red;
      color: white;
      border: none;
      padding: 8px;
      cursor: pointer;
      border-radius: 3px;
      margin-top: 10px;
      width: auto;
    }
    img { max-width: 100%; margin-top: 10px; border-radius: 8px; }
    .form-section { background: #002f5f; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .nav-link { color: gold; text-decoration: none; margin-right: 15px; font-size: 14px; }
    .nav-link:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <div style="text-align: center; margin-bottom: 20px;">
    <a href="/" class="nav-link">← Back to Home</a>
  </div>

  <h1>[ADMIN] Oldbridge Media Admin Panel</h1>

  <div class="form-section">
    <h2>📝 Create Post</h2>
    <input id="title" placeholder="Enter post title" />
    <textarea id="message" placeholder="Enter post message"></textarea>
    <input type="file" id="image" />
    <button onclick="submitPost()">📤 Submit Post</button>
  </div>

  <h2>🗑️ Manage Posts</h2>
  <div id="postList"></div>

  <script>
    const TOKEN = "secret-token-bernard-2025";
    const BASE_URL = "https://old-bridge-backend.onrender.com";

    function submitPost() {
      const title = document.getElementById("title").value.trim();
      const message = document.getElementById("message").value.trim();
      const imageFile = document.getElementById("image").files[0];

      if (!title || !message) {
        alert("Please fill in both title and message.");
        return;
      }

      const formData = new FormData();
      formData.append("title", title);
      formData.append("message", message);
      if (imageFile) {
        formData.append("image", imageFile);
      }

      fetch(BASE_URL + "/api/post", {
        method: "POST",
        headers: {
          "Authorization": TOKEN
        },
        body: formData
      })
      .then(res => res.json())
      .then(data => {
        alert("✅ Post submitted");
        document.getElementById("title").value = "";
        document.getElementById("message").value = "";
        document.getElementById("image").value = "";
        loadPosts();
      })
      .catch(err => alert("Error: " + err));
    }

    function loadPosts() {
      fetch(BASE_URL + "/api/posts")
        .then(res => res.json())
        .then(data => {
          const container = document.getElementById("postList");
          container.innerHTML = "";
          if (!data.posts || !data.posts.length) {
            container.innerHTML = "<p>No posts yet.</p>";
            return;
          }
          data.posts.forEach((post, index) => {
            container.innerHTML += `
              <div class="post">
                <h3>${post.title}</h3>
                <p>${post.message}</p>
                ${post.image ? `<img src="${BASE_URL + post.image}" />` : ''}
                <button class="delete-btn" onclick="deletePost(${index})">🗑️ Delete</button>
              </div>
            `;
          });
        })
        .catch(err => console.error("Error loading posts:", err));
    }

    function deletePost(index) {
      if (!confirm("Are you sure you want to delete this post?")) return;
      
      fetch(BASE_URL + "/api/delete", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": TOKEN
        },
        body: JSON.stringify({ index })
      })
      .then(res => res.json())
      .then(data => {
        alert(data.message || "✅ Post deleted");
        loadPosts();
      })
      .catch(err => alert("Error: " + err));
    }

    loadPosts();
  </script>
</body>
</html>'''

@app.route('/')
def index():
    """Public home page"""
    return INDEX_HTML, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/admin')
def admin():
    """Admin panel page"""
    return ADMIN_HTML, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
