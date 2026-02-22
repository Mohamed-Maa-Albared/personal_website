from flask import Blueprint, jsonify, render_template, request

from app import db
from app.models import About, Message, Project

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Homepage"""
    featured_projects = Project.query.filter_by(featured=True).all()
    about = About.query.first()
    return render_template('index.html', projects=featured_projects, about=about)

@main_bp.route('/projects')
def projects():
    """Projects portfolio page"""
    page = request.args.get('page', 1, type=int)
    projects = Project.query.paginate(page=page, per_page=9)
    return render_template('projects.html', projects=projects)

@main_bp.route('/project/<int:project_id>')
def project_detail(project_id):
    """Individual project detail page"""
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@main_bp.route('/about')
def about():
    """About page"""
    about = About.query.first()
    return render_template('about.html', about=about)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form handling"""
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        
        message = Message(
            name=data.get('name'),
            email=data.get('email'),
            subject=data.get('subject'),
            message=data.get('message')
        )
        
        try:
            db.session.add(message)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Message sent successfully!'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error sending message'}), 500
    
    return render_template('contact.html')

@main_bp.route('/api/projects')
def api_projects():
    """API endpoint for projects list"""
    projects = Project.query.all()
    return jsonify([{
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'technologies': p.technologies.split(',') if p.technologies else [],
        'demo_url': p.demo_url,
        'github_url': p.github_url
    } for p in projects])
    } for p in projects])
