"""
Seed script — Populate the database with Mohamed's projects, experience,
blog posts, and case studies in English (and Arabic translations).

Usage
-----
    python seed.py                      # seed (skips if data exists)
    python seed.py --force              # drop all tables then re-seed
    python seed.py --upgrade-schema     # add new _ar columns to existing DB
    python seed.py --inject blog    data/new_post.json      # inject one record
    python seed.py --inject experience  data/new_exp.json
    python seed.py --inject project     data/new_proj.json

JSON inject format
------------------
Each file must be a single JSON object matching the model fields.
For BlogPost the ``created_at`` field must be an ISO-8601 string or absent.
``highlights`` / ``highlights_ar`` must be pre-serialised JSON arrays.

Example (blog):
    {
        "title": "My new post",
        "title_ar": "مقالتي الجديدة",
        "slug": "my-new-post",
        "excerpt": "Short preview...",
        "excerpt_ar": "معاينة قصيرة...",
        "content": "<p>Body HTML</p>",
        "content_ar": "<p>نص المقال</p>",
        "category": "AI",
        "tags": "AI, Python",
        "read_time": 5,
        "published": true,
        "featured": false,
        "sort_order": 0
    }
"""

import json
import os
import sys
from datetime import datetime, timedelta

from app import create_app, db
from app.models import (
    BlogPost,
    Experience,
    ImpactCard,
    LanguageItem,
    Project,
    SiteConfig,
    SkillCluster,
)

app = create_app(os.environ.get("FLASK_ENV", "development"))

# ═══════════════════════════════════════════════════════════════
# EXPERIENCES
# ═══════════════════════════════════════════════════════════════
EXPERIENCES = [
    {
        "role": "Data Scientist",
        "role_ar": "عالم بيانات",
        "company": "zeroG – AI in Aviation (Lufthansa Group)",
        "location": "Frankfurt, Germany",
        "date_range": "Dec 2022 – Present",
        "description": (
            "Lead the innovation, design, and implementation of advanced AI systems "
            "to drive customer engagement and strategic business initiatives. "
            "Serve as a key resource for Generative and Agentic AI."
        ),
        "description_ar": (
            "أقود ابتكار وتصميم وتنفيذ أنظمة الذكاء الاصطناعي المتقدمة "
            "لتعزيز مشاركة العملاء والمبادرات الاستراتيجية. "
            "أعمل كمرجع رئيسي في مجال الذكاء الاصطناعي التوليدي والعملي."
        ),
        "highlights": json.dumps(
            [
                "<strong>Keynote on Agentic AI</strong> with live multi-agent system demo at Data Community Day",
                "Pioneered first <strong>generative AI 'categories model'</strong> for city destination scoring",
                "Engineered <strong>ancillary recommender</strong> driving <strong>3-15% purchase increase</strong> across airlines",
                "Optimised recommender APIs for up to <strong>20x performance gain</strong>",
                "Built comprehensive <strong>AB testing pipeline</strong> from scratch for rigorous model validation",
            ]
        ),
        "highlights_ar": json.dumps(
            [
                "<strong>كلمة رئيسية عن الذكاء الاصطناعي العملي</strong> مع عرض حي لنظام متعدد الوكلاء في يوم مجتمع البيانات",
                "رائد أول <strong>نموذج فئات بالذكاء الاصطناعي التوليدي</strong> لتقييم وجهات المدن",
                "بناء <strong>نظام توصية إضافي</strong> يرفع معدل الشراء بنسبة <strong>3-15%</strong> عبر شركات الطيران",
                "تحسين أداء واجهات برمجة التطبيقات بمعدل يصل إلى <strong>20 ضعفاً</strong>",
                "إنشاء منظومة <strong>اختبار AB</strong> شاملة من الصفر للتحقق الصارم من النماذج",
            ]
        ),
        "sort_order": 1,
    },
    {
        "role": "AI Engineer (Freelance)",
        "role_ar": "مهندس ذكاء اصطناعي (مستقل)",
        "company": "Freelance",
        "location": "Remote",
        "date_range": "Apr 2021 – Oct 2022",
        "description": (
            "Delivered end-to-end AI solutions for diverse clients, "
            "managing every stage from scoping to deployment and maintenance."
        ),
        "description_ar": (
            "تسليم حلول ذكاء اصطناعي متكاملة لعملاء متنوعين، "
            "مع إدارة كل مرحلة من تحديد النطاق حتى النشر والصيانة."
        ),
        "highlights": json.dumps(
            [
                "<strong>'Virtual Patient'</strong> simulation for interactive medical training",
                "Automated <strong>Dark Web Auto-Labelling & Classification</strong> system",
            ]
        ),
        "highlights_ar": json.dumps(
            [
                "محاكاة <strong>'المريض الافتراضي'</strong> للتدريب الطبي التفاعلي",
                "نظام آلي لـ<strong>التصنيف والوسم التلقائي للويب المظلم</strong>",
            ]
        ),
        "sort_order": 2,
    },
    {
        "role": "Engineering Lecturer (Part-Time)",
        "role_ar": "محاضر هندسة (دوام جزئي)",
        "company": "Arab International University",
        "location": "Damascus, Syria",
        "date_range": "Feb 2022 – Jun 2022",
        "description": (
            "Instructed undergraduate students in Algorithms & Data Structures. "
            "Developed curriculum, projects, and assessments."
        ),
        "description_ar": (
            "تدريس طلاب البكالوريوس في الخوارزميات وهياكل البيانات. "
            "تطوير المناهج والمشاريع والتقييمات."
        ),
        "highlights": json.dumps(
            [
                "<strong>Algorithms & Data Structures</strong> lab instructor",
                "Delivered <strong>Reinforcement Learning</strong> workshop (Smart Tech Institute, 2021)",
            ]
        ),
        "highlights_ar": json.dumps(
            [
                "مدرّب مختبر <strong>الخوارزميات وهياكل البيانات</strong>",
                "تقديم ورشة عمل <strong>التعلم المعزز</strong> (معهد التكنولوجيا الذكية، 2021)",
            ]
        ),
        "sort_order": 3,
    },
    {
        "role": "Data Scientist",
        "role_ar": "عالم بيانات",
        "company": "Damascus-based Start-Up",
        "location": "Damascus, Syria",
        "date_range": "Apr 2020 – Jun 2021",
        "description": (
            "Owned the full data science pipeline, from web scraping and cleaning "
            "to modelling and deployment of predictive systems."
        ),
        "description_ar": (
            "إدارة منظومة علم البيانات الكاملة، من جمع البيانات وتنظيفها "
            "إلى بناء النماذج ونشر الأنظمة التنبؤية."
        ),
        "highlights": json.dumps(
            [
                "<strong>Foreign Exchange Forecasting</strong> (JPY/CAD) – time-series model",
                "<strong>Emotion Prediction from Voice</strong> – deep learning classifier",
                "<strong>Arabic Tweets Classifier</strong> – NLP sentiment analysis",
            ]
        ),
        "highlights_ar": json.dumps(
            [
                "<strong>التنبؤ بأسعار الصرف</strong> (JPY/CAD) – نموذج السلاسل الزمنية",
                "<strong>التنبؤ بالمشاعر من الصوت</strong> – مصنّف تعلم عميق",
                "<strong>مصنّف التغريدات العربية</strong> – تحليل المشاعر بمعالجة اللغة الطبيعية",
            ]
        ),
        "sort_order": 4,
    },
    {
        "role": "BSc Informatics Engineering – AI Major",
        "role_ar": "بكالوريوس هندسة المعلوماتية – تخصص ذكاء اصطناعي",
        "company": "Arab International University",
        "location": "Damascus, Syria",
        "date_range": "Sep 2015 – Mar 2021",
        "description": (
            "Thesis: Human Behavior Simulation – a multi-modal AI system combining "
            "voice cloning, 3D avatar reconstruction, and deep RL agent training."
        ),
        "description_ar": (
            "الأطروحة: محاكاة السلوك البشري – نظام ذكاء اصطناعي متعدد الوسائط "
            "يجمع بين استنساخ الصوت وإعادة بناء الصورة الرمزية ثلاثية الأبعاد "
            "وتدريب وكيل التعلم المعزز العميق."
        ),
        "highlights": json.dumps(
            [
                "<strong>Voice Cloning</strong> via Zero-Shot Learning from 5-20s audio samples",
                "<strong>3D Avatar Reconstruction</strong> using Facebook's PIFu from a single image",
                "<strong>RL Agent</strong> trained to walk in Blender/Unity via PPO",
            ]
        ),
        "highlights_ar": json.dumps(
            [
                "<strong>استنساخ الصوت</strong> عبر Zero-Shot Learning من 5-20 ثانية صوتية",
                "<strong>إعادة بناء صورة رمزية ثلاثية الأبعاد</strong> باستخدام PIFu من Facebook من صورة واحدة",
                "<strong>وكيل التعلم المعزز</strong> مُدرَّب على المشي في Blender/Unity عبر PPO",
            ]
        ),
        "sort_order": 5,
    },
]

# ═══════════════════════════════════════════════════════════════
# PROJECTS
# ═══════════════════════════════════════════════════════════════
PROJECTS = [
    {
        "title": "Multi-Agent Voice System",
        "title_ar": "نظام صوتي متعدد الوكلاء",
        "short_description": "Voice-activated autonomous business analysis.",
        "short_description_ar": "تحليل أعمال مستقل يعمل بالصوت.",
        "description": (
            "Designed and built a live, multi-agent system demo presented as a keynote "
            "at the Lufthansa Group Data Community Day 2025. The system processes voice "
            "commands, transcribes them, and uses an LLM orchestrator to delegate tasks "
            "to specialised search and data analysis agents — solving complex business "
            "queries in real-time."
        ),
        "description_ar": (
            "تصميم وبناء عرض توضيحي حي لنظام متعدد الوكلاء قُدِّم كخطاب رئيسي "
            "في يوم مجتمع بيانات مجموعة لوفتهانزا 2025. يعالج النظام الأوامر الصوتية "
            "ويحوّلها إلى نص، ويستخدم منسّق LLM لتفويض المهام إلى وكلاء البحث "
            "وتحليل البيانات المتخصصين — لحل استفسارات الأعمال المعقدة في الوقت الحقيقي."
        ),
        "technologies": "Python,LLM Orchestration,Whisper,Azure OpenAI,Multi-Agent Systems",
        "category": "genai",
        "year": "2025",
        "client": "Lufthansa Group",
        "featured": True,
        "sort_order": 1,
        "has_case_study": True,
        "challenge": (
            "<p>The Lufthansa Group Data Community Day is the biggest and most sought-after annual data "
            "event in the Group. I was tasked with representing zeroG by delivering an advanced presentation "
            "on Agentic AI and Multi-Agent Systems. The challenge: go beyond slides and build a "
            "<strong>working, voice-activated multi-agent system</strong> that could accept natural "
            "voice commands, reason about the intent, and coordinate multiple "
            "specialised agents to produce actionable business insights — all live on stage "
            "with zero tolerance for failure.</p>"
            "<p>Traditional chatbots fall short here — they can't decompose complex queries, "
            "delegate subtasks, or synthesise information from multiple sources autonomously.</p>"
        ),
        "challenge_ar": (
            "<p>يُعدّ يوم مجتمع بيانات مجموعة لوفتهانزا أكبر حدث بيانات سنوي في المجموعة. "
            "أُسنِد إليّ تمثيل zeroG من خلال تقديم عرض متقدم عن الذكاء الاصطناعي العملي "
            "وأنظمة الوكلاء المتعددة. التحدي: تجاوز الشرائح وبناء "
            "<strong>نظام متعدد الوكلاء يعمل بالصوت</strong> قادر على قبول الأوامر الصوتية "
            "الطبيعية والاستدلال على النية وتنسيق وكلاء متخصصين متعددين لإنتاج رؤى أعمال "
            "قابلة للتنفيذ — كل هذا مباشرة على المسرح بلا هامش للفشل.</p>"
            "<p>روبوتات الدردشة التقليدية تقصر هنا — إذ لا تستطيع تفكيك الاستفسارات المعقدة "
            "أو تفويض المهام الفرعية أو دمج المعلومات من مصادر متعددة باستقلالية.</p>"
        ),
        "approach": (
            "<p>The architecture follows a <strong>hierarchical orchestration pattern</strong>:</p>"
            "<ul>"
            "<li><strong>Voice Layer:</strong> Real-time voice transcription converts spoken commands into text</li>"
            "<li><strong>Orchestrator Agent:</strong> An LLM-powered coordinator that parses intent, decomposes the query "
            "into subtasks, and selects the appropriate specialist agent</li>"
            "<li><strong>Search Agent:</strong> Retrieves relevant information from knowledge bases for research tasks</li>"
            "<li><strong>Data Analysis Agent:</strong> Handles data queries, computes KPIs, and generates insights for business analysis</li>"
            "</ul>"
            '<p>The presentation, titled "LLMs: From Chatty Cathy to Autonomous Agents," walked the audience '
            "through the evolution of AI from simple chatbots to autonomous reasoning systems, culminating "
            "in the live demo.</p>"
        ),
        "approach_ar": (
            "<p>تتبع البنية <strong>نمط التنسيق الهرمي</strong>:</p>"
            "<ul>"
            "<li><strong>طبقة الصوت:</strong> تحويل الأوامر الصوتية إلى نص في الوقت الحقيقي</li>"
            "<li><strong>وكيل المنسّق:</strong> منسّق يعمل بـ LLM يحلل النية ويفكك الاستفسار "
            "إلى مهام فرعية ويختار الوكيل المتخصص المناسب</li>"
            "<li><strong>وكيل البحث:</strong> استرجاع المعلومات ذات الصلة من قواعد المعرفة للمهام البحثية</li>"
            "<li><strong>وكيل تحليل البيانات:</strong> معالجة استفسارات البيانات وحساب مؤشرات الأداء وتوليد الرؤى التحليلية</li>"
            "</ul>"
            "<p>قدّم العرض، المعنون «نماذج اللغة الكبيرة: من المحادثة إلى الوكلاء المستقلين»، "
            "للجمهور مسيرة تطور الذكاء الاصطناعي من روبوتات الدردشة البسيطة إلى أنظمة الاستدلال المستقلة.</p>"
        ),
        "results": (
            "<p>The live demo at Data Community Day 2025 was delivered successfully:</p>"
            "<ul>"
            "<li>Successfully demonstrated <strong>autonomous task delegation</strong> across specialised agents solving a business query in real-time</li>"
            "<li>The presentation <strong>sparked significant discussions</strong> about agentic AI adoption across the organisation</li>"
            "<li>Demonstrated zeroG's <strong>cutting-edge expertise</strong> in autonomous AI systems</li>"
            "<li>This was my <strong>second consecutive year</strong> keynoting at Data Community Day, reinforcing thought leadership</li>"
            "</ul>"
        ),
        "results_ar": (
            "<p>نُفِّذ العرض الحي في يوم مجتمع البيانات 2025 بنجاح:</p>"
            "<ul>"
            "<li>إثبات ناجح لـ<strong>تفويض المهام المستقل</strong> عبر وكلاء متخصصين لحل استفسار أعمال في الوقت الحقيقي</li>"
            "<li>أشعل العرض <strong>نقاشات واسعة</strong> حول تبني الذكاء الاصطناعي العملي في المنظمة</li>"
            "<li>إثبات <strong>الخبرة المتطورة</strong> لـzeroG في أنظمة الذكاء الاصطناعي المستقلة</li>"
            "<li>كان هذا <strong>عامي الثاني على التوالي</strong> في تقديم الخطاب الرئيسي، مما يعزز ريادة الفكر</li>"
            "</ul>"
        ),
        "metrics": json.dumps(
            [
                {"value": "2nd", "label": "Consecutive Year Keynoting"},
                {"value": "Live", "label": "Working Demo on Stage"},
                {"value": "Voice", "label": "Enabled Multi-Agent System"},
                {"value": "3", "label": "Specialised Agents"},
            ]
        ),
    },
    {
        "title": "Ancillary Recommender System",
        "title_ar": "نظام التوصية الإضافية",
        "short_description": "Production recommendation engine driving 3-15% purchase uplift.",
        "short_description_ar": "محرك توصيات إنتاجي يرفع المشتريات بنسبة 3-15%.",
        "description": (
            "Engineered and deployed a production-grade ancillary recommender system "
            "across multiple Lufthansa Group airline partners. The system scores and "
            "ranks ancillary products in real-time, resulting in a measurable 3-15% "
            "increase in purchase rates. Included API refactoring that achieved a 20x "
            "performance gain."
        ),
        "description_ar": (
            "هندسة ونشر نظام توصية إضافي بجودة إنتاجية عبر شركاء شركات طيران متعددة "
            "في مجموعة لوفتهانزا. يقيّم النظام المنتجات الإضافية ويرتبها في الوقت الحقيقي، "
            "مما أسفر عن زيادة قابلة للقياس في معدلات الشراء بنسبة 3-15%. "
            "تضمّن إعادة هيكلة واجهة برمجة التطبيقات لتحقيق مكسب أداء بمقدار 20 ضعفاً."
        ),
        "technologies": "Python,Scikit-Learn,Azure ML,REST APIs,AB Testing",
        "category": "recsys",
        "year": "2023",
        "client": "Lufthansa Group",
        "featured": True,
        "sort_order": 2,
        "has_case_study": True,
        "challenge": (
            "<p>Airline ancillary products (seat upgrades, baggage, meals, etc.) represent a significant revenue "
            "stream, but generic 'one-size-fits-all' product listings miss the mark. The challenge was to "
            "<strong>personalise ancillary product recommendations</strong> at scale across "
            "multiple airline partners — each with different product catalogues, touchpoints, and "
            "purchasing patterns.</p>"
            "<p>Additionally, the existing recommender API was too slow for real-time deployment "
            "across critical customer touchpoints.</p>"
        ),
        "challenge_ar": (
            "<p>تمثّل المنتجات الإضافية للطيران (ترقيات المقاعد والأمتعة والوجبات وغيرها) مصدر إيرادات "
            "مهماً، لكن قوائم المنتجات العامة لا تُحقق الهدف. كان التحدي "
            "<strong>تخصيص توصيات المنتجات الإضافية</strong> على نطاق واسع عبر "
            "شركاء شركات طيران متعددة — كل منها بكتالوجات منتجات ونقاط تواصل وأنماط شراء مختلفة.</p>"
            "<p>علاوة على ذلك، كانت واجهة برمجة تطبيقات التوصية الحالية بطيئة جداً للنشر الفوري "
            "عبر نقاط التواصل الحرجة مع العملاء.</p>"
        ),
        "approach": (
            "<p>Engineered a production recommendation system with full lifecycle ownership:</p>"
            "<ul>"
            "<li><strong>Scoring Model:</strong> Built the ancillary recommender scoring system to rank products "
            "based on customer and booking context</li>"
            "<li><strong>API Optimisation:</strong> Re-factored the ancillary recommender APIs to achieve "
            "a 20x performance gain, enabling real-time use across customer touchpoints</li>"
            "<li><strong>AB Testing:</strong> Validated impact through rigorous experimentation with "
            "the AB testing framework (evaluation still ongoing for different airlines)</li>"
            "<li><strong>Cross-Team Adoption:</strong> Successfully influenced another product team "
            "to adopt the centralised API, preventing redundant development and saving resources</li>"
            "</ul>"
        ),
        "approach_ar": (
            "<p>هندسة نظام توصية إنتاجي مع الملكية الكاملة لدورة حياته:</p>"
            "<ul>"
            "<li><strong>نموذج التقييم:</strong> بناء نظام تقييم الموصيات الإضافية لترتيب المنتجات "
            "بناءً على سياق العميل والحجز</li>"
            "<li><strong>تحسين الواجهة البرمجية:</strong> إعادة هيكلة واجهات برمجة تطبيقات الموصيات "
            "الإضافية لتحقيق مكسب أداء بمقدار 20 ضعفاً، مما يتيح الاستخدام الفوري عبر نقاط التواصل</li>"
            "<li><strong>اختبار AB:</strong> التحقق من التأثير من خلال تجارب صارمة مع إطار اختبار AB</li>"
            "<li><strong>التبني عبر الفرق:</strong> التأثير بنجاح على فريق منتجات آخر لاعتماد الواجهة البرمجية المركزية</li>"
            "</ul>"
        ),
        "results": (
            "<p>Deployed across multiple Lufthansa Group airlines with measurable impact:</p>"
            "<ul>"
            "<li><strong>3-15% increase in ancillary purchases</strong> across different touchpoints and devices</li>"
            "<li><strong>20x API performance gain</strong> enabling real-time recommendations</li>"
            "<li>Destination recommender APIs also optimised for a <strong>2x performance gain</strong></li>"
            "<li>Influenced another team to adopt the centralised API, preventing duplicate development</li>"
            "</ul>"
        ),
        "results_ar": (
            "<p>تم النشر عبر شركات طيران متعددة في مجموعة لوفتهانزا مع تأثير قابل للقياس:</p>"
            "<ul>"
            "<li><strong>زيادة بنسبة 3-15% في مشتريات الإضافات</strong> عبر نقاط التواصل والأجهزة المختلفة</li>"
            "<li><strong>مكسب أداء الواجهة البرمجية بمقدار 20 ضعفاً</strong> يتيح التوصيات الفورية</li>"
            "<li>تحسين واجهات برمجة موصيات الوجهات أيضاً بـ<strong>مكسب أداء مضاعف</strong></li>"
            "<li>التأثير على فريق آخر لاعتماد الواجهة البرمجية المركزية والحدّ من تكرار التطوير</li>"
            "</ul>"
        ),
        "metrics": json.dumps(
            [
                {"value": "3-15%", "label": "Purchase Uplift"},
                {"value": "20x", "label": "Ancillary API Speedup"},
                {"value": "2x", "label": "Destination API Speedup"},
                {"value": "Multi", "label": "Airline Partners"},
            ]
        ),
    },
    {
        "title": "Generative AI City Recommender",
        "title_ar": "موصي المدن بالذكاء الاصطناعي التوليدي",
        "short_description": "First GenAI model for destination scoring & diversity.",
        "short_description_ar": "أول نموذج ذكاء اصطناعي توليدي لتقييم الوجهات وتنوعها.",
        "description": (
            "Pioneered the first generative AI-based 'categories model' to score city "
            "destinations. The model significantly improved the diversity and relevance "
            "of travel recommendations by combining category embeddings with frequency- "
            "based signals, serving the 95%+ non-logged-in customer base."
        ),
        "description_ar": (
            "رائد أول 'نموذج فئات' يعتمد على الذكاء الاصطناعي التوليدي لتقييم وجهات المدن. "
            "حسّن النموذج بشكل ملحوظ تنوع وملاءمة توصيات السفر من خلال دمج تضمينات الفئات "
            "مع إشارات قائمة على التردد، لخدمة أكثر من 95% من قاعدة العملاء غير المسجلين."
        ),
        "technologies": "Python,Generative AI,Azure OpenAI,Pandas,NumPy",
        "category": "genai",
        "year": "2024",
        "client": "Lufthansa Group",
        "featured": True,
        "sort_order": 3,
        "has_case_study": True,
        "challenge": (
            "<p>Over <strong>95% of visitors</strong> to Lufthansa Group websites are non-logged-in users. "
            "Traditional collaborative filtering is impossible due to the cold-start problem. "
            "The existing frequency-table model served generic, popularity-biased recommendations "
            "that lacked diversity and relevance.</p>"
        ),
        "challenge_ar": (
            "<p>أكثر من <strong>95% من الزوار</strong> لمواقع مجموعة لوفتهانزا هم مستخدمون غير مسجلين. "
            "الفلترة التعاونية التقليدية مستحيلة بسبب مشكلة البدء البارد. "
            "كان النموذج الحالي القائم على جدول التردد يقدم توصيات عامة متحيزة للشعبية "
            "تفتقر إلى التنوع والملاءمة.</p>"
        ),
        "approach": (
            "<p>Pioneered an innovative approach combining generative AI with the existing frequency table:</p>"
            "<ul>"
            "<li><strong>Category Model:</strong> Used generative AI to score city destinations with "
            "nuanced category profiles, creating the first GenAI-based model in the recommendation system</li>"
            "<li><strong>Integration Strategy:</strong> Picked the top categories for each city, then "
            "recommended similar cities based on shared top categories — combining the category model "
            "with the frequency table using an innovative approach</li>"
            "<li><strong>Diversity:</strong> The category-based approach naturally improved recommendation "
            "diversity by surfacing destinations that match user interests rather than just popularity</li>"
            "</ul>"
        ),
        "approach_ar": (
            "<p>رائد نهج مبتكر يجمع الذكاء الاصطناعي التوليدي مع جدول التردد الحالي:</p>"
            "<ul>"
            "<li><strong>نموذج الفئات:</strong> استخدام الذكاء الاصطناعي التوليدي لتقييم وجهات المدن "
            "بملفات تعريف فئوية دقيقة، مما يُنشئ أول نموذج قائم على الذكاء الاصطناعي التوليدي في نظام التوصية</li>"
            "<li><strong>استراتيجية التكامل:</strong> اختيار أبرز الفئات لكل مدينة، ثم توصية مدن مماثلة "
            "بناءً على الفئات المشتركة — بدمج نموذج الفئات مع جدول التردد بنهج مبتكر</li>"
            "<li><strong>التنوع:</strong> حسّن النهج القائم على الفئات تنوع التوصية طبيعياً "
            "بتسليط الضوء على الوجهات التي تطابق اهتمامات المستخدم لا الشعبية فحسب</li>"
            "</ul>"
        ),
        "results": (
            "<p>Transformed destination recommendations for the majority of website visitors:</p>"
            "<ul>"
            "<li>Significantly <strong>improved diversity and relevance</strong> of destination recommendations</li>"
            "<li>Served the <strong>95%+ non-logged-in customer base</strong> that the previous model underserved</li>"
            "<li>First successful application of <strong>generative AI within the recommendation system</strong></li>"
            "<li>Enhanced the previously underperforming frequency table model through improved category integration</li>"
            "</ul>"
        ),
        "results_ar": (
            "<p>حوّل توصيات الوجهات لغالبية زوار الموقع:</p>"
            "<ul>"
            "<li><strong>تحسين ملحوظ في تنوع وملاءمة</strong> توصيات الوجهات</li>"
            "<li>خدمة <strong>قاعدة العملاء غير المسجلين البالغة 95%+</strong> التي كافح النموذج السابق في خدمتها</li>"
            "<li>أول تطبيق ناجح للـ<strong>ذكاء الاصطناعي التوليدي داخل نظام التوصية</strong></li>"
            "<li>تعزيز نموذج جدول التردد الضعيف سابقاً من خلال تكامل أفضل للفئات</li>"
            "</ul>"
        ),
        "metrics": json.dumps(
            [
                {"value": "95%+", "label": "Traffic Served"},
                {"value": "1st", "label": "GenAI in RecSys"},
                {"value": "↑", "label": "Recommendation Diversity"},
                {"value": "↑", "label": "Relevance vs Frequency Table"},
            ]
        ),
    },
    {
        "title": "AB Testing Framework",
        "title_ar": "إطار اختبار AB",
        "short_description": "Comprehensive experimentation pipeline with causal inference.",
        "short_description_ar": "منظومة تجريب شاملة مع الاستدلال السببي.",
        "description": (
            "Led research and development of a comprehensive, generalised AB testing framework. "
            "Includes covariate balance checking, ATE analysis, and a sophisticated CATE framework "
            "with five meta-learners, SHAP-based customer archetype discovery, and automated "
            "dual-reporting (technical and stakeholder)."
        ),
        "description_ar": (
            "قيادة البحث والتطوير لإطار اختبار AB شامل ومعمّم. "
            "يتضمن فحص توازن المتغيرات المشتركة، وتحليل ATE، وإطار CATE متطور "
            "مع خمسة متعلّمات تلوية، واكتشاف نماذج العملاء القائم على SHAP، "
            "وتقارير مزدوجة آلية (تقنية وللمساهمين)."
        ),
        "technologies": "Python,Causal Inference,SHAP,Meta-Learners,Statistical Testing",
        "category": "recsys",
        "year": "2024",
        "client": "Lufthansa Group",
        "featured": False,
        "sort_order": 4,
    },
    {
        "title": "Human Behavior Simulation",
        "title_ar": "محاكاة السلوك البشري",
        "short_description": "Multi-modal AI: voice cloning + 3D avatar + RL agent.",
        "short_description_ar": "ذكاء اصطناعي متعدد الوسائط: استنساخ صوت + صورة رمزية ثلاثية الأبعاد + وكيل RL.",
        "description": (
            "Master's thesis combining three AI modalities: Zero-Shot voice cloning, "
            "3D avatar reconstruction (PIFu), and deep RL agent training (PPO)."
        ),
        "description_ar": (
            "أطروحة الماجستير تجمع بين ثلاثة وسائط للذكاء الاصطناعي: "
            "استنساخ الصوت بـZero-Shot، وإعادة بناء الصورة الرمزية ثلاثية الأبعاد (PIFu)، "
            "وتدريب وكيل التعلم المعزز العميق (PPO)."
        ),
        "technologies": "Python,TensorFlow,Blender,Unity,C#,PPO",
        "category": "rl cv",
        "year": "2021",
        "client": "Arab International University",
        "featured": False,
        "sort_order": 5,
    },
    {
        "title": "Virtual Patient Simulation",
        "title_ar": "محاكاة المريض الافتراضي",
        "short_description": "Interactive AI patient for medical training scenarios.",
        "short_description_ar": "مريض ذكاء اصطناعي تفاعلي لسيناريوهات التدريب الطبي.",
        "description": (
            "Developed an AI-powered 'Virtual Patient' simulation for interactive "
            "clinical training."
        ),
        "description_ar": (
            "تطوير محاكاة 'مريض افتراضي' مدعومة بالذكاء الاصطناعي للتدريب السريري التفاعلي."
        ),
        "technologies": "Python,NLP,SGD,Classification,Flask",
        "category": "nlp",
        "year": "2022",
        "client": "Freelance Client",
        "featured": False,
        "sort_order": 6,
    },
    {
        "title": "Dark Web Auto-Labelling",
        "title_ar": "الوسم التلقائي للويب المظلم",
        "short_description": "Automated classification of dark web content.",
        "short_description_ar": "تصنيف آلي لمحتوى الويب المظلم.",
        "description": (
            "Built an automated system for scraping, labelling, and classifying dark web "
            "content using NLP-based text classification pipelines."
        ),
        "description_ar": (
            "بناء نظام آلي لجمع ووسم وتصنيف محتوى الويب المظلم "
            "باستخدام منظومات تصنيف النصوص المعتمدة على معالجة اللغة الطبيعية."
        ),
        "technologies": "Python,Scikit-Learn,BeautifulSoup,Selenium,NLP",
        "category": "nlp",
        "year": "2022",
        "client": "Freelance Client",
        "featured": False,
        "sort_order": 7,
    },
    {
        "title": "Emotion Prediction from Voice",
        "title_ar": "التنبؤ بالمشاعر من الصوت",
        "short_description": "Deep learning classifier for vocal emotion detection.",
        "short_description_ar": "مصنّف تعلم عميق للكشف عن المشاعر الصوتية.",
        "description": (
            "Deep learning model predicting human emotions (calm, happy, sad, angry, fearful, "
            "surprised, disgusted) from audio files using Inception networks on mel-spectrograms."
        ),
        "description_ar": (
            "نموذج تعلم عميق يتنبأ بالمشاعر البشرية (هادئ، سعيد، حزين، غاضب، خائف، "
            "مفاجأ، مشمئز) من الملفات الصوتية باستخدام شبكات Inception على الطيف الصوتي."
        ),
        "technologies": "Python,TensorFlow,Keras,Inception,Mel-Spectrogram",
        "category": "cv",
        "year": "2021",
        "client": "Damascus Start-Up",
        "featured": False,
        "sort_order": 8,
    },
    {
        "title": "Arabic Tweets Classifier",
        "title_ar": "مصنّف التغريدات العربية",
        "short_description": "Sentiment analysis for Arabic social media text.",
        "short_description_ar": "تحليل المشاعر لنصوص وسائل التواصل الاجتماعي العربية.",
        "description": (
            "Kaggle competition for classifying Arabic tweets into positive, negative, and neutral "
            "sentiment classes. Achieved 75.9% accuracy using BERT with extensive Arabic language processing."
        ),
        "description_ar": (
            "مسابقة Kaggle لتصنيف التغريدات العربية إلى فئات المشاعر الإيجابية والسلبية والمحايدة. "
            "حققت دقة 75.9% باستخدام BERT مع معالجة شاملة للغة العربية."
        ),
        "technologies": "Python,BERT,Arabic NLP,Kaggle",
        "category": "nlp",
        "year": "2021",
        "client": "Damascus Start-Up",
        "featured": False,
        "sort_order": 9,
    },
    {
        "title": "Forex Forecasting (JPY/CAD)",
        "title_ar": "التنبؤ بأسعار صرف العملات (JPY/CAD)",
        "short_description": "Time-series model for foreign exchange prediction.",
        "short_description_ar": "نموذج سلاسل زمنية للتنبؤ بأسعار الصرف.",
        "description": (
            "Predicting JPY/CAD exchange rates using 20 years of scraped economic data from "
            "multiple websites and Reuters news. Combined macroeconomic features from Japan, "
            "Canada, and the USA with deep neural networks for prediction."
        ),
        "description_ar": (
            "التنبؤ بأسعار صرف JPY/CAD باستخدام 20 عاماً من البيانات الاقتصادية المجمّعة "
            "من مواقع متعددة وأخبار رويترز. دمج المؤشرات الاقتصادية الكلية من اليابان "
            "وكندا والولايات المتحدة مع الشبكات العصبية العميقة للتنبؤ."
        ),
        "technologies": "Python,TensorFlow,Web Scraping,Reuters NLP,Deep NN",
        "category": "nlp",
        "year": "2020",
        "client": "Damascus Start-Up",
        "featured": False,
        "sort_order": 10,
    },
    {
        "title": "RAG Pipeline with Smart Segmentation",
        "title_ar": "منظومة RAG مع التجزئة الذكية",
        "short_description": "Retrieval-Augmented Generation with semantic chunking.",
        "short_description_ar": "توليد معزز بالاسترجاع مع التقسيم الدلالي للنصوص.",
        "description": (
            "RAG pipeline with smart document segmentation inspired by Anthropic's "
            "research, dynamically chunking documents based on semantic boundaries."
        ),
        "description_ar": (
            "منظومة RAG مع تجزئة ذكية للوثائق مستوحاة من أبحاث Anthropic، "
            "تقسّم الوثائق ديناميكياً بناءً على الحدود الدلالية."
        ),
        "technologies": "Python,LangChain,FAISS,Azure OpenAI",
        "category": "genai",
        "year": "2024",
        "client": "Personal Project",
        "featured": False,
        "sort_order": 11,
    },
    {
        "title": "AI Search & Reasoning Agents",
        "title_ar": "وكلاء البحث والاستدلال بالذكاء الاصطناعي",
        "short_description": "Multi-step reasoning agents inspired by OpenAI O-series.",
        "short_description_ar": "وكلاء استدلال متعدد الخطوات مستلهمة من OpenAI O-series.",
        "description": (
            "Multi-step reasoning AI agents with source credibility assessment, "
            "chain-of-thought reasoning, and autonomous tool use."
        ),
        "description_ar": (
            "وكلاء ذكاء اصطناعي للاستدلال متعدد الخطوات مع تقييم مصداقية المصادر، "
            "والتفاوض الفكري المتسلسل، واستخدام الأدوات باستقلالية."
        ),
        "technologies": "Python,LangChain,OpenAI,Tool Use,Agents",
        "category": "genai",
        "year": "2024",
        "client": "Personal Project",
        "featured": False,
        "sort_order": 12,
    },
]


# ═══════════════════════════════════════════════════════════════
# BLOG POSTS
# ═══════════════════════════════════════════════════════════════
BLOG_POSTS = [
    {
        "title": "The Architecture of Thought: How Neuroscience Is Inspiring the Next Wave of AI Agents",
        "title_ar": "بنيان الفكر: كيف يُلهم علم الأعصاب الجيل القادم من وكلاء الذكاء الاصطناعي",
        "slug": "architecture-of-thought-neuroscience-ai-agents",
        "category": "Neuroscience",
        "tags": "Neuroscience,Agentic AI,Multi-Agent Systems,Prefrontal Cortex,LLM Orchestration",
        "read_time": 12,
        "featured": True,
        "published": True,
        "sort_order": 1,
        "excerpt": (
            "Your prefrontal cortex is the world's most sophisticated AI orchestrator — delegating tasks, "
            "managing working memory, and coordinating specialised brain regions. Recent neuroscience reveals "
            "striking parallels with modern multi-agent AI architectures."
        ),
        "excerpt_ar": (
            "قشرتك الجبهية الأمامية هي أكثر منسّقات الذكاء الاصطناعي احترافاً في العالم — تفوّض المهام، "
            "وتدير الذاكرة العاملة، وتنسّق مناطق دماغية متخصصة. يكشف علم الأعصاب الحديث "
            "عن تشابهات مذهلة مع بنيات الذكاء الاصطناعي متعددة الوكلاء."
        ),
        "content": "<h2>The Brain's Original Multi-Agent Architecture</h2>\n<p>When I built a <strong>multi-agent voice system</strong> for Lufthansa Group's Data Community Day — a system where an LLM orchestrator delegates tasks to specialised search and data analysis agents — I wasn't just engineering software. I was, unknowingly, replicating one of the brain's oldest design patterns.</p>\n<p>The prefrontal cortex (PFC) doesn't do everything itself. It's an <em>executive coordinator</em> — remarkably similar to the orchestrator agent pattern now dominating AI system design. And recent neuroscience research reveals just how deep this parallel runs.</p>\n<h2>The Prefrontal Cortex as Orchestrator</h2>\n<p>A landmark 2024 study published in <em>Nature Neuroscience</em> by Rigotti et al. demonstrated that prefrontal neurons exhibit <strong>\"mixed selectivity\"</strong> — they respond to complex combinations of task variables rather than single features. This is strikingly similar to how LLM-based orchestrators process multi-dimensional context before deciding which specialist to invoke.</p>\n<p>Here's what most people don't realize: <strong>your brain runs on roughly 20 watts of power</strong> — less than a laptop charger. Yet it coordinates approximately 86 billion neurons across hundreds of specialised regions, maintaining coherent behaviour through what neuroscientists call <em>hierarchical predictive processing</em>.</p>\n<blockquote>\n<p>\"The brain doesn't process information — it <em>predicts</em> it. Every neural circuit is running a generative model of the world, constantly updating its predictions against incoming sensory data.\"</p>\n<p>— Karl Friston, Free Energy Principle</p>\n</blockquote>\n<h2>Surprising Parallel: Attention in Brains and Transformers</h2>\n<p>The transformer architecture's <strong>attention mechanism</strong> — the foundation of every modern LLM — bears a remarkable resemblance to the brain's selective attention system. In 2023, researchers at DeepMind and UCL showed that the mathematical operations underlying multi-head attention are functionally equivalent to what hippocampal place cells do when navigating spatial environments.</p>\n<h2>The Workspace Theory: What Consciousness Teaches AI</h2>\n<p>Cognitive scientist Bernard Baars proposed the <strong>Global Workspace Theory (GWT)</strong> of consciousness in the 1980s — the idea that consciousness emerges from a \"workspace\" where specialised cognitive modules compete for access to broadcast their information globally.</p>\n<h2>Engineering Lessons</h2>\n<ol>\n<li><strong>Delegation over computation:</strong> The brain doesn't compute everything centrally. Neither should your AI system. Specialise and delegate.</li>\n<li><strong>Prediction over reaction:</strong> The most efficient systems anticipate rather than respond. Build predictive models, not just reactive pipelines.</li>\n<li><strong>Error signals over raw data:</strong> The brain transmits surprises, not observations. Design systems that focus on what's unexpected.</li>\n</ol>",
        "content_ar": '<h2>البنية الأصلية للدماغ متعددة الوكلاء</h2>\n<p>حين بنيت <strong>نظام صوتي متعدد الوكلاء</strong> ليوم مجتمع بيانات مجموعة لوفتهانزا — نظام يفوّض فيه منسّق LLM المهام إلى وكلاء بحث وتحليل بيانات متخصصة — لم أكن أطوّر برمجيات فحسب. كنت، دون أن أدري، أُعيد إنتاج أحد أقدم أنماط تصميم الدماغ.</p>\n<p>القشرة الجبهية الأمامية (PFC) لا تفعل كل شيء بنفسها. إنها <em>منسّق تنفيذي</em> — تشبه بشكل لافت نمط وكيل المنسّق الذي يهيمن الآن على تصميم أنظمة الذكاء الاصطناعي.</p>\n<h2>القشرة الجبهية الأمامية كمنسّق</h2>\n<p>كشفت دراسة بارزة نُشرت عام 2024 في <em>Nature Neuroscience</em> أن الخلايا العصبية الجبهية تُظهر <strong>"الانتقائية المختلطة"</strong> — حيث تستجيب لمجموعات معقدة من متغيرات المهمة لا لسمة واحدة. هذا مشابه بشكل لافت لكيفية معالجة المنسّقات القائمة على LLM للسياق متعدد الأبعاد قبل تحديد الوكيل المناسب.</p>\n<h2>نظرية الفضاء العالمي: ما يعلّمنا الوعي عن الذكاء الاصطناعي</h2>\n<p>اقترح عالم الإدراك برنارد بارس <strong>نظرية مساحة العمل العالمية (GWT)</strong> للوعي في الثمانينيات — فكرة أن الوعي ينشأ من "مساحة عمل" تتنافس فيها الوحدات المعرفية المتخصصة للوصول وبث معلوماتها عالمياً.</p>\n<h2>دروس هندسية</h2>\n<ol>\n<li><strong>التفويض على الحساب:</strong> الدماغ لا يحسب كل شيء مركزياً. كذلك لا ينبغي لنظام الذكاء الاصطناعي. تخصّص وفوّض.</li>\n<li><strong>التنبؤ على ردّ الفعل:</strong> الأنظمة الأكثر كفاءة تتوقع بدلاً من أن تستجيب.</li>\n<li><strong>إشارات الخطأ على البيانات الخام:</strong> الدماغ ينقل المفاجآت لا الملاحظات. صمّم أنظمة تركّز على ما هو غير متوقع.</li>\n</ol>',
        "created_at": datetime(2026, 2, 15),
    },
    {
        "title": "From Chatty Cathy to Autonomous Reasoners: The Agentic AI Revolution",
        "title_ar": "من روبوتات الدردشة إلى العقلاء المستقلين: ثورة الذكاء الاصطناعي العملي",
        "slug": "agentic-ai-revolution-autonomous-reasoners",
        "category": "AI",
        "tags": "Agentic AI,LLM,Autonomous Agents,ReAct,Tool Use,Reasoning",
        "read_time": 10,
        "featured": True,
        "published": True,
        "sort_order": 2,
        "excerpt": (
            "We're witnessing the most fundamental shift in AI since deep learning: "
            "the transition from models that chat to systems that reason, plan, and act. "
            "Here's what's really happening behind the hype — and what I've learned building these systems."
        ),
        "excerpt_ar": (
            "نشهد أعمق تحوّل في الذكاء الاصطناعي منذ التعلم العميق: "
            "الانتقال من نماذج تتحدث إلى أنظمة تستدل وتخطط وتتصرف. "
            "إليك ما يحدث فعلاً وراء الضجيج — وما تعلمته من بناء هذه الأنظمة."
        ),
        "content": '<h2>The Quiet Revolution</h2>\n<p>In 2023, you asked an LLM a question and it answered. In 2024, you asked it to accomplish a goal and it wrote code. In 2025, you described a <em>problem</em> and it assembled a team of agents to solve it autonomously.</p>\n<p>This isn\'t incremental progress. It\'s a phase transition. And having built one of these systems live on stage — <strong>a voice-activated multi-agent system for the Lufthansa Group Data Community Day</strong> — I can tell you the gap between "chatbot" and "autonomous agent" is larger than most people appreciate.</p>\n<h2>What Actually Changed?</h2>\n<h3>1. Reliable Tool Use</h3>\n<p>The moment LLMs could <strong>reliably call functions</strong> — querying databases, invoking APIs, running code — they stopped being conversationalists and became operators.</p>\n<h3>2. Chain-of-Thought Reasoning</h3>\n<p>The publication of <strong>ReAct (Reasoning + Acting)</strong> by Yao et al. showed that interleaving reasoning traces with action steps dramatically improved task completion rates.</p>\n<h3>3. Multi-Agent Coordination</h3>\n<p>Single agents hit a ceiling quickly. The breakthrough came from <strong>splitting responsibilities</strong> across specialised agents — mirroring how human organisations work.</p>\n<h2>What Most People Get Wrong</h2>\n<h3>The Reliability Problem</h3>\n<p>"Demo-quality" agent systems fail spectacularly in production. A system that works 90% of the time in a demo fails roughly <strong>every 10th customer interaction</strong>.</p>\n<h3>Latency Is the Silent Killer</h3>\n<p>Multi-step agent reasoning introduces <strong>compounding latency</strong>. Each LLM call adds 1-3 seconds. The solution isn\'t faster models — it\'s better <strong>architecture</strong>.</p>\n<h2>Where This Is Going</h2>\n<ol>\n<li><strong>Agent Operating Systems:</strong> Standardised platforms for agents with process management, memory systems, and inter-agent communication. MCP is an early example.</li>\n<li><strong>Specialised Agent Hardware:</strong> New silicon optimised for frequent, small, context-heavy calls.</li>\n<li><strong>Agent-Native Applications:</strong> Applications where the entire UX is built around an autonomous agent.</li>\n</ol>',
        "content_ar": '<h2>الثورة الهادئة</h2>\n<p>في 2023، كنت تسأل نموذج لغوياً فيجيب. في 2024، طلبت منه إنجاز هدف فكتب كوداً. في 2025، وصفت <em>مشكلة</em> فجمّع فريقاً من الوكلاء لحلها باستقلالية.</p>\n<p>هذا ليس تقدماً تدريجياً. إنه تحوّل جذري. وبعد أن بنيت أحد هذه الأنظمة على المسرح مباشرة — <strong>نظام صوتي متعدد الوكلاء ليوم مجتمع بيانات مجموعة لوفتهانزا</strong> — أستطيع القول إن الهوة بين "روبوت الدردشة" و"الوكيل المستقل" أضخم مما يُقدِّر معظم الناس.</p>\n<h2>ما الذي تغيّر فعلاً؟</h2>\n<h3>1. استخدام الأدوات بموثوقية</h3>\n<p>في اللحظة التي أصبحت فيها نماذج اللغة الكبيرة قادرة على <strong>استدعاء الدوال بموثوقية</strong> — استعلام قواعد البيانات، واستدعاء الواجهات البرمجية، وتشغيل الكود — توقفت عن كونها محادِثة وأصبحت مشغِّلة.</p>\n<h3>2. الاستدلال بسلسلة الأفكار</h3>\n<p>أظهر نشر <strong>ReAct (الاستدلال + التصرف)</strong> بواسطة Yao et al. أن التناوب بين آثار الاستدلال وخطوات التصرف حسّن بشكل كبير معدلات إتمام المهام.</p>\n<h3>3. تنسيق الوكلاء المتعددين</h3>\n<p>الوكلاء الفرديون يصطدمون بسقف سريعاً. جاء الاختراق من <strong>تقسيم المسؤوليات</strong> عبر وكلاء متخصصين — مرايا لكيفية عمل المنظمات البشرية.</p>\n<h2>إلى أين يسير هذا؟</h2>\n<ol>\n<li><strong>أنظمة تشغيل الوكلاء:</strong> منصات معيارية مع إدارة العمليات وأنظمة الذاكرة وبروتوكولات التواصل بين الوكلاء. MCP مثال مبكر.</li>\n<li><strong>أجهزة الوكلاء المتخصصة:</strong> شرائح جديدة محسّنة للاستدعاءات الصغيرة والمتكررة والمحمّلة بالسياق.</li>\n<li><strong>تطبيقات أصيلة للوكلاء:</strong> تطبيقات يُبنى فيها تجربة المستخدم بالكامل حول وكيل مستقل.</li>\n</ol>',
        "created_at": datetime(2026, 2, 1),
    },
    {
        "title": "The Neural Canvas: Where Art, Neuroscience, and AI Converge",
        "title_ar": "اللوحة العصبية: حيث يتلاقى الفن وعلم الأعصاب والذكاء الاصطناعي",
        "slug": "neural-canvas-art-neuroscience-ai",
        "category": "Art",
        "tags": "Neuroaesthetics,Generative Art,Neural Style Transfer,Creativity,GANs,Voice Cloning",
        "read_time": 14,
        "featured": True,
        "published": True,
        "sort_order": 3,
        "excerpt": (
            "Your brain's visual cortex uses operations remarkably similar to convolutional neural networks. "
            "Beauty activates the same reward circuits as food and sex. And AI is now creating art that triggers "
            "genuine aesthetic experiences. The convergence of these fields is revealing something profound."
        ),
        "excerpt_ar": (
            "القشرة البصرية في دماغك تستخدم عمليات مشابهة بشكل ملحوظ للشبكات العصبية التلافيفية. "
            "الجمال يُنشّط دوائر المكافأة ذاتها كالطعام. والذكاء الاصطناعي يبتكر الآن فناً يُثير "
            "تجارب جمالية حقيقية. يكشف تلاقي هذه المجالات عن شيء عميق."
        ),
        "content": "<h2>When Your Brain Looks at Art, It's Running a Neural Network</h2>\n<p>In 2014, neuroscientist Semir Zeki published a finding that would bridge two worlds: when humans experience beauty — whether in visual art, music, or mathematical equations — it activates a specific region of the medial orbito-frontal cortex. The same region. Every time.</p>\n<p>This wasn't just a curious observation. It suggested something radical: <strong>beauty is a computation</strong>, not just a feeling.</p>\n<h2>The Hidden Mathematics of Visual Perception</h2>\n<p>Here's something that most people don't realize: <strong>the primate visual cortex was the direct inspiration for convolutional neural networks (CNNs)</strong>.</p>\n<p>In 1962, Hubel and Wiesel discovered that neurons in the visual cortex are organised hierarchically:</p>\n<ul>\n<li><strong>V1 (primary visual cortex):</strong> Detects edges and orientations — exactly like the first layers of a CNN</li>\n<li><strong>V4:</strong> Processes colour and complex forms — analogous to deeper feature maps</li>\n<li><strong>IT (inferotemporal cortex):</strong> Recognises objects and faces — like the final classification layers</li>\n</ul>\n<h2>GANs: The Brain's Own Generative Model</h2>\n<p>Generative Adversarial Networks mirror a fascinating aspect of brain function. The brain actively <strong>generates predictions</strong> about what it expects to see, then compares against actual input. This is essentially the GAN architecture: a generator (cortical prediction) and a discriminator (error detection).</p>\n<h2>The Future: Computational Creativity</h2>\n<p>For the first time, we have AI systems that can <em>generate</em> aesthetic content, neuroscience tools that can <em>measure</em> aesthetic experience, and mathematical frameworks to <em>model</em> the relationship. The neural canvas is being painted from both sides: biology and silicon.</p>",
        "content_ar": "<h2>حين ينظر دماغك إلى الفن، فهو يشغّل شبكة عصبية</h2>\n<p>في عام 2014، نشر عالم الأعصاب سمير زيكي اكتشافاً يجسر عالمين: حين يختبر البشر الجمال — سواء في الفن البصري أو الموسيقى أو المعادلات الرياضية — فإنه يُنشّط منطقة محددة في القشرة الحجاجية الأمامية الوسطى. المنطقة ذاتها. في كل مرة.</p>\n<p>لم يكن هذا مجرد ملاحظة فضولية. إنه يُشير إلى شيء جذري: <strong>الجمال عملية حسابية</strong>، لا مجرد شعور.</p>\n<h2>الرياضيات الخفية للإدراك البصري</h2>\n<p>شيء لا يدركه معظم الناس: <strong>القشرة البصرية للرئيسيات كانت مصدر الإلهام المباشر للشبكات العصبية التلافيفية (CNNs)</strong>.</p>\n<p>في عام 1962، اكتشف هيوبل وويزل أن الخلايا العصبية في القشرة البصرية منظّمة هرمياً:</p>\n<ul>\n<li><strong>V1 (القشرة البصرية الأولية):</strong> تكشف الحواف والاتجاهات — تماماً كالطبقات الأولى في CNN</li>\n<li><strong>V4:</strong> تعالج الألوان والأشكال المعقدة — مشابهة لخرائط الميزات العميقة</li>\n<li><strong>IT (القشرة الصدغية السفلية):</strong> تتعرف على الأجسام والوجوه — كالطبقات التصنيفية النهائية</li>\n</ul>\n<h2>الشبكات التوليدية التنافسية: النموذج التوليدي للدماغ</h2>\n<p>تعكس GANs جانباً رائعاً من وظيفة الدماغ. الدماغ يُولّد بنشاط <strong>تنبؤات</strong> بما يتوقع رؤيته، ثم يقارنها بالمدخلات الفعلية. هذه هي بنية GAN في جوهرها: مولّد (التنبؤ القشري) ومُميِّز (كشف الأخطاء).</p>\n<h2>المستقبل: الإبداع الحسابي</h2>\n<p>للمرة الأولى، لدينا أنظمة ذكاء اصطناعي تستطيع <em>توليد</em> المحتوى الجمالي، وأدوات علم الأعصاب التي تستطيع <em>قياس</em> التجربة الجمالية، وأُطر رياضية لـ<em>نمذجة</em> العلاقة. اللوحة العصبية تُرسم من الجانبين: البيولوجيا والسيليكون.</p>",
        "created_at": datetime(2026, 1, 15),
    },
    {
        "title": "Recommendation Systems at 30,000 Feet: Engineering Serendipity in Aviation",
        "title_ar": "أنظمة التوصية على ارتفاع 30,000 قدم: هندسة المصادفة السعيدة في الطيران",
        "slug": "recommendation-systems-aviation-engineering-serendipity",
        "category": "AI",
        "tags": "Recommendation Systems,Aviation,Cold Start,AB Testing,Personalisation,Machine Learning",
        "read_time": 11,
        "featured": False,
        "published": True,
        "sort_order": 4,
        "excerpt": (
            "Building recommendation systems for airlines is nothing like Netflix or Spotify. "
            "95% of users are anonymous, purchases are infrequent and high-stakes, and a 'wrong' "
            "recommendation can cost real money. Here's what I learned engineering serendipity in aviation."
        ),
        "excerpt_ar": (
            "بناء أنظمة التوصية للطيران لا يشبه Netflix أو Spotify في شيء. "
            "95% من المستخدمين مجهولون، والمشتريات نادرة وعالية المخاطر، والتوصية 'الخاطئة' "
            "قد تُكلّف أموالاً حقيقية. إليك ما تعلمته من هندسة المصادفة السعيدة في قطاع الطيران."
        ),
        "content": "<h2>This Is Not Netflix</h2>\n<p>When people think \"recommendation systems,\" they think Netflix suggesting movies or Spotify building playlists. These scenarios share a key advantage: <strong>abundant user data</strong>.</p>\n<p>Now imagine building a recommendation system where:</p>\n<ul>\n<li><strong>95% of your users are completely anonymous</strong></li>\n<li>The average user interacts <strong>2-3 times per year</strong></li>\n<li>A single purchase can cost <strong>hundreds or thousands of euros</strong></li>\n</ul>\n<p>Welcome to airline recommendation systems. This has been my world at zeroG (Lufthansa Group) for the past three years.</p>\n<h2>The Cold Start Problem at Scale</h2>\n<p>For most platforms, cold-start users are 10-20% of traffic. For airlines, it's <strong>95%+</strong>.</p>\n<h2>The Art of Measuring Impact</h2>\n<p>Building the recommendation system was hard. <strong>Proving it worked</strong> was harder. I built an AB testing framework from the ground up handling two different segmentation paradigms.</p>\n<p>The key insight: <strong>statistical significance doesn't equal business significance</strong>.</p>\n<h2>The 20x Optimisation</h2>\n<p>The biggest improvement wasn't a better model — it was a better <strong>API architecture</strong>. Vectorised scoring, connection pooling, response caching, and lazy loading achieved a <strong>20x performance improvement</strong>.</p>",
        "content_ar": '<h2>هذا ليس Netflix</h2>\n<p>حين يفكر الناس في "أنظمة التوصية"، يفكرون في اقتراحات Netflix للأفلام أو Spotify في قوائم التشغيل. تشترك هذه السيناريوهات في ميزة رئيسية: <strong>بيانات مستخدم وفيرة</strong>.</p>\n<p>الآن تخيّل بناء نظام توصية حيث:</p>\n<ul>\n<li><strong>95% من مستخدميك مجهولون تماماً</strong></li>\n<li>يتفاعل المستخدم العادي <strong>2-3 مرات سنوياً</strong> فقط</li>\n<li>قد تُكلّف عملية الشراء الواحدة <strong>مئات أو آلاف اليوروهات</strong></li>\n</ul>\n<p>مرحباً بك في أنظمة توصية شركات الطيران. كان هذا عالمي في zeroG (مجموعة لوفتهانزا) على مدى السنوات الثلاث الماضية.</p>\n<h2>مشكلة البدء البارد على نطاق واسع</h2>\n<p>لمعظم المنصات، يشكّل مستخدمو البدء البارد 10-20% من الحركة. لشركات الطيران، هم <strong>أكثر من 95%</strong>.</p>\n<h2>فن قياس التأثير</h2>\n<p>بناء نظام التوصية كان صعباً. <strong>إثبات نجاحه</strong> كان أصعب. بنيت إطار اختبار AB من الصفر يتعامل مع نموذجَين مختلفَين للتجزئة.</p>\n<p>الرؤية الرئيسية: <strong>الأهمية الإحصائية لا تساوي الأهمية التجارية</strong>.</p>\n<h2>تحسين الأداء بمقدار 20 ضعفاً</h2>\n<p>أكبر تحسين لم يكن نموذجاً أفضل — بل <strong>بنية واجهة برمجية أفضل</strong>. حققت التقييم المتجهي والتجمع وتخزين الاستجابات مؤقتاً والتحميل الكسول <strong>تحسيناً في الأداء بمقدار 20 ضعفاً</strong>.</p>',
        "created_at": datetime(2025, 12, 20),
    },
]


# ═══════════════════════════════════════════════════════════════
# SITE CONFIGS  (bilingual — Arabic variants stored as _ar keys)
# ═══════════════════════════════════════════════════════════════
SITE_CONFIGS = [
    # ── Hero Section ──
    {
        "key": "hero_label",
        "value": "DATA SCIENTIST &bull; AI ENGINEER",
        "label": "Label / Title Bar",
        "group": "hero",
    },
    {
        "key": "hero_label_ar",
        "value": "عالم بيانات &bull; مهندس ذكاء اصطناعي",
        "label": "Label / Title Bar (AR)",
        "group": "hero",
    },
    {
        "key": "hero_name_line1",
        "value": "MOHAMED",
        "label": "Name Line 1",
        "group": "hero",
    },
    {
        "key": "hero_name_line2",
        "value": "MAA ALBARED",
        "label": "Name Line 2",
        "group": "hero",
    },
    {
        "key": "hero_tagline_word1",
        "value": "Architecting",
        "label": "Tagline Word 1",
        "group": "hero",
    },
    {
        "key": "hero_tagline_word1_ar",
        "value": "بناء",
        "label": "Tagline Word 1 (AR)",
        "group": "hero",
    },
    {
        "key": "hero_tagline_word2",
        "value": "Intelligence",
        "label": "Tagline Word 2",
        "group": "hero",
    },
    {
        "key": "hero_tagline_word2_ar",
        "value": "الذكاء",
        "label": "Tagline Word 2 (AR)",
        "group": "hero",
    },
    {
        "key": "hero_subtitle",
        "value": "Where neural networks meet creative intuition – building systems that reason, collaborate, and act.",
        "label": "Subtitle",
        "group": "hero",
    },
    {
        "key": "hero_subtitle_ar",
        "value": "حيث تلتقي الشبكات العصبية بالحدس الإبداعي — نبني أنظمة تستدل وتتعاون وتتصرف.",
        "label": "Subtitle (AR)",
        "group": "hero",
    },
    # ── About Section ──
    {
        "key": "about_bio1",
        "value": "Accomplished Data Scientist with over <strong>4 years of experience</strong> specializing in the development and deployment of machine learning and generative AI solutions within the <strong>aviation sector</strong>.",
        "label": "Bio Paragraph 1",
        "group": "about",
    },
    {
        "key": "about_bio1_ar",
        "value": "عالم بيانات متمرس بأكثر من <strong>4 سنوات من الخبرة</strong> في تطوير ونشر حلول التعلم الآلي والذكاء الاصطناعي التوليدي في <strong>قطاع الطيران</strong>.",
        "label": "Bio Paragraph 1 (AR)",
        "group": "about",
    },
    {
        "key": "about_bio2",
        "value": "Proven track record of driving significant business value by architecting <strong>recommendation systems</strong>, optimizing model performance by up to <strong>20x</strong>, and pioneering <strong>AB testing frameworks</strong> from the ground up.",
        "label": "Bio Paragraph 2",
        "group": "about",
    },
    {
        "key": "about_bio2_ar",
        "value": "سجل موثوق في توليد قيمة تجارية ملموسة من خلال هندسة <strong>أنظمة التوصية</strong>، وتحسين أداء النماذج بما يصل إلى <strong>20 ضعفاً</strong>، ورعاية <strong>أُطر اختبار AB</strong> من الصفر.",
        "label": "Bio Paragraph 2 (AR)",
        "group": "about",
    },
    {
        "key": "about_bio3",
        "value": "Recognized as a subject matter expert in <strong>LLM orchestration</strong> and <strong>autonomous agent design</strong>, adept at translating complex AI capabilities into strategic, impactful business outcomes.",
        "label": "Bio Paragraph 3",
        "group": "about",
    },
    {
        "key": "about_bio3_ar",
        "value": "معترف به كخبير متخصص في <strong>تنسيق نماذج اللغة الكبيرة</strong> و<strong>تصميم الوكلاء المستقلين</strong>، ماهر في ترجمة قدرات الذكاء الاصطناعي المعقدة إلى نتائج تجارية استراتيجية مؤثرة.",
        "label": "Bio Paragraph 3 (AR)",
        "group": "about",
    },
    {
        "key": "about_years",
        "value": "4",
        "label": "Years of Experience",
        "group": "about",
    },
    {
        "key": "about_projects_count",
        "value": "50+",
        "label": "Projects Delivered",
        "group": "about",
    },
    {
        "key": "about_perf_gains",
        "value": "20",
        "label": "Performance Gains (x)",
        "group": "about",
    },
]


# ═══════════════════════════════════════════════════════════════
# IMPACT CARDS
# ═══════════════════════════════════════════════════════════════
IMPACT_CARDS = [
    {
        "icon": "&#9883;",
        "value": "15",
        "prefix": "",
        "suffix": "%",
        "description": "Ancillary purchase lift across airline partners",
        "description_ar": "زيادة في مشتريات الإضافات عبر شركاء شركات الطيران",
        "sort_order": 1,
    },
    {
        "icon": "&#9889;",
        "value": "20",
        "prefix": "",
        "suffix": "x",
        "description": "Recommender API speedup for real-time scoring",
        "description_ar": "تسريع واجهة برمجة الموصيات للتقييم الفوري",
        "sort_order": 2,
    },
    {
        "icon": "&#9992;",
        "value": "6",
        "prefix": "",
        "suffix": "+",
        "description": "Airlines served with personalized recommendations",
        "description_ar": "شركات طيران تخدمها توصيات مخصصة",
        "sort_order": 3,
    },
    {
        "icon": "&#9733;",
        "value": "2",
        "prefix": "",
        "suffix": "x",
        "description": "Keynote presenter at the biggest LHG data event",
        "description_ar": "متحدث رئيسي في أكبر حدث بيانات في مجموعة لوفتهانزا",
        "sort_order": 4,
    },
]


# ═══════════════════════════════════════════════════════════════
# SKILL CLUSTERS
# ═══════════════════════════════════════════════════════════════
SKILL_CLUSTERS = [
    {
        "icon": "&#129302;",
        "title": "Generative & Agentic AI",
        "title_ar": "الذكاء الاصطناعي التوليدي والعملي",
        "tags": "LLM Orchestration, Multi-Agent Systems, Prompt Engineering, RAG Pipelines, Fine-Tuning, LangChain/LangGraph, Semantic Kernel",
        "tags_ar": "تنسيق نماذج اللغة، أنظمة متعددة الوكلاء، هندسة الأوامر، خطوط RAG، الضبط الدقيق، LangChain/LangGraph، Semantic Kernel",
        "sort_order": 1,
    },
    {
        "icon": "&#129504;",
        "title": "ML & Data Science",
        "title_ar": "التعلم الآلي وعلم البيانات",
        "tags": "Recommendation Systems, NLP/NLU, Classification, Regression, Feature Engineering, A/B Testing, XGBoost, Deep Learning",
        "tags_ar": "أنظمة التوصية، معالجة اللغة الطبيعية، التصنيف، الانحدار، هندسة الميزات، اختبار A/B، XGBoost، التعلم العميق",
        "sort_order": 2,
    },
    {
        "icon": "&#128187;",
        "title": "Tech Stack",
        "title_ar": "المنظومة التقنية",
        "tags": "Python, SQL, Flask, FastAPI, TensorFlow, PyTorch, scikit-learn, Pandas, NumPy, Git, REST APIs",
        "tags_ar": "بايثون، SQL، Flask، FastAPI، TensorFlow، PyTorch، scikit-learn، Pandas، NumPy، Git، REST APIs",
        "sort_order": 3,
    },
    {
        "icon": "&#9729;",
        "title": "Cloud & MLOps",
        "title_ar": "الحوسبة السحابية وعمليات التعلم الآلي",
        "tags": "Azure ML, AWS (S3, Lambda), Docker, CI/CD, MLflow, Weights & Biases, Databricks, Airflow",
        "tags_ar": "Azure ML، AWS (S3، Lambda)، Docker، CI/CD، MLflow، Weights & Biases، Databricks، Airflow",
        "sort_order": 4,
    },
]


# ═══════════════════════════════════════════════════════════════
# LANGUAGES
# ═══════════════════════════════════════════════════════════════
LANGUAGE_ITEMS = [
    {"name": "Arabic", "level": "Native", "sort_order": 1},
    {"name": "English", "level": "C1-C2", "sort_order": 2},
    {"name": "German", "level": "A2", "sort_order": 3},
]


# ─────────────────────────────────────────────────────────────────────────────
# Schema migration helper  (adds new _ar columns to an existing database)
# ─────────────────────────────────────────────────────────────────────────────

_AR_SCHEMA_MIGRATIONS = [
    # (table, column, sql_type)
    ("projects", "title_ar", "TEXT"),
    ("projects", "short_description_ar", "TEXT"),
    ("projects", "description_ar", "TEXT"),
    ("projects", "challenge_ar", "TEXT"),
    ("projects", "approach_ar", "TEXT"),
    ("projects", "results_ar", "TEXT"),
    ("projects", "case_study_ar", "TEXT"),
    ("experiences", "role_ar", "TEXT"),
    ("experiences", "description_ar", "TEXT"),
    ("experiences", "highlights_ar", "TEXT"),
    ("blog_posts", "title_ar", "TEXT"),
    ("blog_posts", "excerpt_ar", "TEXT"),
    ("blog_posts", "content_ar", "TEXT"),
    ("impact_cards", "description_ar", "TEXT"),
    ("skill_clusters", "title_ar", "TEXT"),
    ("skill_clusters", "tags_ar", "TEXT"),
]


def upgrade_schema():
    """Add all ``_ar`` columns to an existing database (idempotent).

    Safe to run on a live SQLite or PostgreSQL database.  Uses
    ``ADD COLUMN IF NOT EXISTS`` (PostgreSQL) or catches the duplicate-column
    error (SQLite) so it is completely idempotent.
    """
    from sqlalchemy import text

    with app.app_context():
        dialect = db.engine.dialect.name  # 'sqlite' or 'postgresql'
        with db.engine.connect() as conn:
            for table, column, sql_type in _AR_SCHEMA_MIGRATIONS:
                try:
                    if dialect == "postgresql":
                        conn.execute(
                            text(
                                f"ALTER TABLE {table} ADD COLUMN IF NOT EXISTS"
                                f" {column} {sql_type}"
                            )
                        )
                    else:
                        # SQLite does not support IF NOT EXISTS on ALTER TABLE
                        conn.execute(
                            text(f"ALTER TABLE {table} ADD COLUMN {column} {sql_type}")
                        )
                    print(f"  + {table}.{column}")
                except Exception as exc:
                    msg = str(exc).lower()
                    if "duplicate column" in msg or "already exists" in msg:
                        print(f"  ✓ {table}.{column} (already exists)")
                    else:
                        raise
            conn.commit()
    print("Schema upgrade complete.")


# ─────────────────────────────────────────────────────────────────────────────
# Content injection helpers (--inject CLI)
# ─────────────────────────────────────────────────────────────────────────────


def _coerce_bool(v):
    if isinstance(v, bool):
        return v
    return str(v).lower() in ("1", "true", "yes")


def inject_blog(data: dict):
    """Insert or update a single blog post from a dict.

    If a post with the same slug already exists it is *updated*.
    All HTML fields are sanitised before saving.
    """
    from app.utils import generate_slug, sanitize_html, sanitize_input

    with app.app_context():
        title = sanitize_input(data["title"], 300)
        slug = data.get("slug") or generate_slug(title)

        post = BlogPost.query.filter_by(slug=slug).first()
        is_new = post is None
        if is_new:
            post = BlogPost()

        created_at_raw = data.get("created_at")
        if created_at_raw and isinstance(created_at_raw, str):
            try:
                post.created_at = datetime.fromisoformat(created_at_raw)
            except ValueError:
                pass

        post.title = title
        post.title_ar = sanitize_input(data.get("title_ar", ""), 300)
        post.slug = sanitize_input(slug, 300)
        post.excerpt = sanitize_input(data.get("excerpt", ""), 500)
        post.excerpt_ar = sanitize_input(data.get("excerpt_ar", ""), 500)
        post.content = sanitize_html(data.get("content", ""))
        post.content_ar = sanitize_html(data.get("content_ar", ""))
        post.cover_image = sanitize_input(data.get("cover_image", ""), 500)
        post.category = sanitize_input(data.get("category", ""), 100)
        post.tags = sanitize_input(data.get("tags", ""), 500)
        post.read_time = int(data.get("read_time", 5))
        post.published = _coerce_bool(data.get("published", True))
        post.featured = _coerce_bool(data.get("featured", False))
        post.sort_order = int(data.get("sort_order", 0))

        if is_new:
            db.session.add(post)
        db.session.commit()
        verb = "Created" if is_new else "Updated"
        print(f"{verb} blog post: '{post.title}' (slug={post.slug})")


def inject_experience(data: dict):
    """Insert a single experience entry from a dict (always creates new)."""
    import json as _json

    from app.utils import sanitize_html, sanitize_input

    with app.app_context():
        highlights_raw = data.get("highlights", "[]")
        highlights_ar_raw = data.get("highlights_ar", "[]")

        # Accept pre-serialised JSON string or a Python list
        if isinstance(highlights_raw, list):
            highlights_raw = _json.dumps(highlights_raw)
        if isinstance(highlights_ar_raw, list):
            highlights_ar_raw = _json.dumps(highlights_ar_raw)

        exp = Experience(
            role=sanitize_input(data["role"], 200),
            role_ar=sanitize_input(data.get("role_ar", ""), 200),
            company=sanitize_input(data["company"], 200),
            location=sanitize_input(data.get("location", ""), 200),
            date_range=sanitize_input(data["date_range"], 100),
            description=sanitize_input(data.get("description", ""), 2000),
            description_ar=sanitize_input(data.get("description_ar", ""), 2000),
            highlights=highlights_raw,
            highlights_ar=highlights_ar_raw,
            sort_order=int(data.get("sort_order", 0)),
        )
        db.session.add(exp)
        db.session.commit()
        print(f"Created experience: '{exp.role}' at {exp.company}")


def inject_project(data: dict):
    """Insert or update a single project from a dict.

    If a project with the same title already exists it is *updated*.
    """
    from app.utils import sanitize_html, sanitize_input

    with app.app_context():
        title = sanitize_input(data["title"], 200)
        proj = Project.query.filter_by(title=title).first()
        is_new = proj is None
        if is_new:
            proj = Project()

        proj.title = title
        proj.title_ar = sanitize_input(data.get("title_ar", ""), 200)
        proj.short_description = sanitize_input(data.get("short_description", ""), 300)
        proj.short_description_ar = sanitize_input(
            data.get("short_description_ar", ""), 300
        )
        proj.description = sanitize_input(data.get("description", ""), 5000)
        proj.description_ar = sanitize_input(data.get("description_ar", ""), 5000)
        proj.technologies = sanitize_input(data.get("technologies", ""), 500)
        proj.category = sanitize_input(data.get("category", ""), 100)
        proj.year = sanitize_input(data.get("year", ""), 20)
        proj.client = sanitize_input(data.get("client", ""), 200)
        proj.image_url = sanitize_input(data.get("image_url", ""), 500)
        proj.demo_url = sanitize_input(data.get("demo_url", ""), 500)
        proj.github_url = sanitize_input(data.get("github_url", ""), 500)
        proj.featured = _coerce_bool(data.get("featured", False))
        proj.sort_order = int(data.get("sort_order", 0))
        proj.has_case_study = _coerce_bool(data.get("has_case_study", False))
        proj.challenge = sanitize_html(data.get("challenge", ""))
        proj.challenge_ar = sanitize_html(data.get("challenge_ar", ""))
        proj.approach = sanitize_html(data.get("approach", ""))
        proj.approach_ar = sanitize_html(data.get("approach_ar", ""))
        proj.results = sanitize_html(data.get("results", ""))
        proj.results_ar = sanitize_html(data.get("results_ar", ""))
        proj.case_study = sanitize_html(data.get("case_study", ""))
        proj.case_study_ar = sanitize_html(data.get("case_study_ar", ""))
        proj.metrics = sanitize_input(data.get("metrics", "[]"), 5000)

        if is_new:
            db.session.add(proj)
        db.session.commit()
        verb = "Created" if is_new else "Updated"
        print(f"{verb} project: '{proj.title}'")


# ─────────────────────────────────────────────────────────────────────────────
# Main seed function
# ─────────────────────────────────────────────────────────────────────────────


def seed():
    with app.app_context():
        db.create_all()

        # Skip seeding if data already exists (preserves admin-added content)
        if Project.query.first() is not None:
            print("Database already has data — skipping seed.")
            print("To force re-seed, run:  python seed.py --force")
            return

        for exp_data in EXPERIENCES:
            db.session.add(Experience(**exp_data))

        for proj_data in PROJECTS:
            db.session.add(Project(**proj_data))

        for post_data in BLOG_POSTS:
            db.session.add(BlogPost(**post_data))

        for cfg_data in SITE_CONFIGS:
            db.session.add(SiteConfig(**cfg_data))

        for card_data in IMPACT_CARDS:
            db.session.add(ImpactCard(**card_data))

        for cluster_data in SKILL_CLUSTERS:
            db.session.add(SkillCluster(**cluster_data))

        for lang_data in LANGUAGE_ITEMS:
            db.session.add(LanguageItem(**lang_data))

        db.session.commit()
        print(
            f"Seeded {len(EXPERIENCES)} experiences, "
            f"{len(PROJECTS)} projects, "
            f"{len(BLOG_POSTS)} blog posts, "
            f"{len(SITE_CONFIGS)} site config entries, "
            f"{len(IMPACT_CARDS)} impact cards, "
            f"{len(SKILL_CLUSTERS)} skill clusters, and "
            f"{len(LANGUAGE_ITEMS)} languages."
        )


# ─────────────────────────────────────────────────────────────────────────────
# Arabic translation backfill
# ─────────────────────────────────────────────────────────────────────────────


def update_ar_translations():
    """Back-fill _ar columns on existing DB rows using seed data.

    Only sets a field when the current DB value is NULL or empty —
    never overwrites content that was set via the admin panel.
    Safe to run on every deploy (idempotent).
    """
    with app.app_context():
        updated = 0

        # ── Experiences: match by role + company ─────────────────────────────
        for data in EXPERIENCES:
            exp = Experience.query.filter_by(
                role=data["role"], company=data["company"]
            ).first()
            if exp is None:
                continue
            for field in ("role_ar", "description_ar", "highlights_ar"):
                if data.get(field) and not getattr(exp, field, None):
                    setattr(exp, field, data[field])
                    updated += 1

        # ── Projects: match by English title ─────────────────────────────────
        for data in PROJECTS:
            proj = Project.query.filter_by(title=data["title"]).first()
            if proj is None:
                continue
            for field in (
                "title_ar",
                "short_description_ar",
                "description_ar",
                "challenge_ar",
                "approach_ar",
                "results_ar",
                "case_study_ar",
            ):
                if data.get(field) and not getattr(proj, field, None):
                    setattr(proj, field, data[field])
                    updated += 1

        # ── Blog posts: match by slug ─────────────────────────────────────────
        for data in BLOG_POSTS:
            post = BlogPost.query.filter_by(slug=data["slug"]).first()
            if post is None:
                continue
            for field in ("title_ar", "excerpt_ar", "content_ar"):
                if data.get(field) and not getattr(post, field, None):
                    setattr(post, field, data[field])
                    updated += 1

        # ── Impact cards: match by sort_order ────────────────────────────────
        for data in IMPACT_CARDS:
            card = ImpactCard.query.filter_by(sort_order=data["sort_order"]).first()
            if card is None:
                continue
            if data.get("description_ar") and not getattr(card, "description_ar", None):
                card.description_ar = data["description_ar"]
                updated += 1

        # ── Skill clusters: match by English title ────────────────────────────
        for data in SKILL_CLUSTERS:
            cluster = SkillCluster.query.filter_by(title=data["title"]).first()
            if cluster is None:
                continue
            for field in ("title_ar", "tags_ar"):
                if data.get(field) and not getattr(cluster, field, None):
                    setattr(cluster, field, data[field])
                    updated += 1

        # ── SiteConfig _ar keys ───────────────────────────────────────────────
        for data in SITE_CONFIGS:
            key = data["key"]
            if key.endswith("_ar") and not SiteConfig.get(key, ""):
                SiteConfig.set(key, data["value"])
                updated += 1

        db.session.commit()
        print(f"update_ar_translations: {updated} field(s) updated.")


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = sys.argv[1:]

    # ── --upgrade-schema ─────────────────────────────────────────────────────
    if "--upgrade-schema" in args:
        print("Running schema upgrade (adding _ar columns)…")
        upgrade_schema()
        sys.exit(0)

    # ── --inject <entity> <json_file> ─────────────────────────────────────────
    if "--inject" in args:
        idx = args.index("--inject")
        if len(args) < idx + 3:
            print("Usage: python seed.py --inject <entity> <json_file>")
            print("       entity: blog | experience | project")
            sys.exit(1)
        entity = args[idx + 1].lower()
        json_path = args[idx + 2]
        with open(json_path, encoding="utf-8") as fh:
            payload = json.load(fh)
        # Support both a single dict or a list of dicts
        records = payload if isinstance(payload, list) else [payload]
        for record in records:
            if entity == "blog":
                inject_blog(record)
            elif entity == "experience":
                inject_experience(record)
            elif entity == "project":
                inject_project(record)
            else:
                print(f"Unknown entity '{entity}'. Choose: blog, experience, project")
                sys.exit(1)
        sys.exit(0)

    # ── --force ───────────────────────────────────────────────────────────────
    if "--force" in args:
        with app.app_context():
            db.drop_all()
            db.create_all()
            print("Force re-seed: all tables dropped and recreated.")

    # Always run schema upgrade first so new _ar columns exist before seeding.
    # upgrade_schema() is idempotent (ADD COLUMN IF NOT EXISTS), so this is
    # safe on every deploy whether or not the columns already exist.
    upgrade_schema()
    seed()
    # Back-fill _ar columns on existing rows (no-op if already populated).
    update_ar_translations()
    sys.exit(0)


EXPERIENCES = [
    {
        "role": "Data Scientist",
        "company": "zeroG – AI in Aviation (Lufthansa Group)",
        "location": "Frankfurt, Germany",
        "date_range": "Dec 2022 – Present",
        "description": (
            "Lead the innovation, design, and implementation of advanced AI systems "
            "to drive customer engagement and strategic business initiatives. "
            "Serve as a key resource for Generative and Agentic AI."
        ),
        "highlights": json.dumps(
            [
                "<strong>Keynote on Agentic AI</strong> with live multi-agent system demo at Data Community Day",
                "Pioneered first <strong>generative AI 'categories model'</strong> for city destination scoring",
                "Engineered <strong>ancillary recommender</strong> driving <strong>3-15% purchase increase</strong> across airlines",
                "Optimised recommender APIs for up to <strong>20x performance gain</strong>",
                "Built comprehensive <strong>AB testing pipeline</strong> from scratch for rigorous model validation",
            ]
        ),
        "sort_order": 1,
    },
    {
        "role": "AI Engineer (Freelance)",
        "company": "Freelance",
        "location": "Remote",
        "date_range": "Apr 2021 – Oct 2022",
        "description": (
            "Delivered end-to-end AI solutions for diverse clients, "
            "managing every stage from scoping to deployment and maintenance."
        ),
        "highlights": json.dumps(
            [
                "<strong>'Virtual Patient'</strong> simulation for interactive medical training",
                "Automated <strong>Dark Web Auto-Labelling & Classification</strong> system",
            ]
        ),
        "sort_order": 2,
    },
    {
        "role": "Engineering Lecturer (Part-Time)",
        "company": "Arab International University",
        "location": "Damascus, Syria",
        "date_range": "Feb 2022 – Jun 2022",
        "description": (
            "Instructed undergraduate students in Algorithms & Data Structures. "
            "Developed curriculum, projects, and assessments."
        ),
        "highlights": json.dumps(
            [
                "<strong>Algorithms & Data Structures</strong> lab instructor",
                "Delivered <strong>Reinforcement Learning</strong> workshop (Smart Tech Institute, 2021)",
            ]
        ),
        "sort_order": 3,
    },
    {
        "role": "Data Scientist",
        "company": "Damascus-based Start-Up",
        "location": "Damascus, Syria",
        "date_range": "Apr 2020 – Jun 2021",
        "description": (
            "Owned the full data science pipeline, from web scraping and cleaning "
            "to modelling and deployment of predictive systems."
        ),
        "highlights": json.dumps(
            [
                "<strong>Foreign Exchange Forecasting</strong> (JPY/CAD) – time-series model",
                "<strong>Emotion Prediction from Voice</strong> – deep learning classifier",
                "<strong>Arabic Tweets Classifier</strong> – NLP sentiment analysis",
            ]
        ),
        "sort_order": 4,
    },
    {
        "role": "BSc Informatics Engineering – AI Major",
        "company": "Arab International University",
        "location": "Damascus, Syria",
        "date_range": "Sep 2015 – Mar 2021",
        "description": (
            "Thesis: Human Behavior Simulation – a multi-modal AI system combining "
            "voice cloning, 3D avatar reconstruction, and deep RL agent training."
        ),
        "highlights": json.dumps(
            [
                "<strong>Voice Cloning</strong> via Zero-Shot Learning from 5-20s audio samples",
                "<strong>3D Avatar Reconstruction</strong> using Facebook's PIFu from a single image",
                "<strong>RL Agent</strong> trained to walk in Blender/Unity via PPO",
            ]
        ),
        "sort_order": 5,
    },
]

PROJECTS = [
    {
        "title": "Multi-Agent Voice System",
        "short_description": "Voice-activated autonomous business analysis.",
        "description": (
            "Designed and built a live, multi-agent system demo presented as a keynote "
            "at the Lufthansa Group Data Community Day 2025. The system processes voice "
            "commands, transcribes them, and uses an LLM orchestrator to delegate tasks "
            "to specialised search and data analysis agents — solving complex business "
            "queries in real-time."
        ),
        "technologies": "Python,LLM Orchestration,Whisper,Azure OpenAI,Multi-Agent Systems",
        "category": "genai",
        "year": "2025",
        "client": "Lufthansa Group",
        "featured": True,
        "sort_order": 1,
        "has_case_study": True,
        "challenge": (
            "<p>The Lufthansa Group Data Community Day is the biggest and most sought-after annual data "
            "event in the Group. I was tasked with representing zeroG by delivering an advanced presentation "
            "on Agentic AI and Multi-Agent Systems. The challenge: go beyond slides and build a "
            "<strong>working, voice-activated multi-agent system</strong> that could accept natural "
            "voice commands, reason about the intent, and coordinate multiple "
            "specialised agents to produce actionable business insights — all live on stage "
            "with zero tolerance for failure.</p>"
            "<p>Traditional chatbots fall short here — they can't decompose complex queries, "
            "delegate subtasks, or synthesise information from multiple sources autonomously.</p>"
        ),
        "approach": (
            "<p>The architecture follows a <strong>hierarchical orchestration pattern</strong>:</p>"
            "<ul>"
            "<li><strong>Voice Layer:</strong> Real-time voice transcription converts spoken commands into text</li>"
            "<li><strong>Orchestrator Agent:</strong> An LLM-powered coordinator that parses intent, decomposes the query "
            "into subtasks, and selects the appropriate specialist agent</li>"
            "<li><strong>Search Agent:</strong> Retrieves relevant information from knowledge bases for research tasks</li>"
            "<li><strong>Data Analysis Agent:</strong> Handles data queries, computes KPIs, and generates insights for business analysis</li>"
            "</ul>"
            '<p>The presentation, titled "LLMs: From Chatty Cathy to Autonomous Agents," walked the audience '
            "through the evolution of AI from simple chatbots to autonomous reasoning systems, culminating "
            "in the live demo.</p>"
        ),
        "results": (
            "<p>The live demo at Data Community Day 2025 was delivered successfully:</p>"
            "<ul>"
            "<li>Successfully demonstrated <strong>autonomous task delegation</strong> across specialised agents solving a business query in real-time</li>"
            "<li>The presentation <strong>sparked significant discussions</strong> about agentic AI adoption across the organisation</li>"
            "<li>Demonstrated zeroG's <strong>cutting-edge expertise</strong> in autonomous AI systems</li>"
            "<li>This was my <strong>second consecutive year</strong> keynoting at Data Community Day, reinforcing thought leadership</li>"
            "</ul>"
        ),
        "metrics": json.dumps(
            [
                {"value": "2nd", "label": "Consecutive Year Keynoting"},
                {"value": "Live", "label": "Working Demo on Stage"},
                {"value": "Voice", "label": "Enabled Multi-Agent System"},
                {"value": "3", "label": "Specialised Agents"},
            ]
        ),
    },
    {
        "title": "Ancillary Recommender System",
        "short_description": "Production recommendation engine driving 3-15% purchase uplift.",
        "description": (
            "Engineered and deployed a production-grade ancillary recommender system "
            "across multiple Lufthansa Group airline partners. The system scores and "
            "ranks ancillary products in real-time, resulting in a measurable 3-15% "
            "increase in purchase rates. Included API refactoring that achieved a 20x "
            "performance gain."
        ),
        "technologies": "Python,Scikit-Learn,Azure ML,REST APIs,AB Testing",
        "category": "recsys",
        "year": "2023",
        "client": "Lufthansa Group",
        "featured": True,
        "sort_order": 2,
        "has_case_study": True,
        "challenge": (
            "<p>Airline ancillary products (seat upgrades, baggage, meals, etc.) represent a significant revenue "
            "stream, but generic 'one-size-fits-all' product listings miss the mark. The challenge was to "
            "<strong>personalise ancillary product recommendations</strong> at scale across "
            "multiple airline partners — each with different product catalogues, touchpoints, and "
            "purchasing patterns.</p>"
            "<p>Additionally, the existing recommender API was too slow for real-time deployment "
            "across critical customer touchpoints.</p>"
        ),
        "approach": (
            "<p>Engineered a production recommendation system with full lifecycle ownership:</p>"
            "<ul>"
            "<li><strong>Scoring Model:</strong> Built the ancillary recommender scoring system to rank products "
            "based on customer and booking context</li>"
            "<li><strong>API Optimisation:</strong> Re-factored the ancillary recommender APIs to achieve "
            "a 20x performance gain, enabling real-time use across customer touchpoints</li>"
            "<li><strong>AB Testing:</strong> Validated impact through rigorous experimentation with "
            "the AB testing framework (evaluation still ongoing for different airlines)</li>"
            "<li><strong>Cross-Team Adoption:</strong> Successfully influenced another product team "
            "to adopt the centralised API, preventing redundant development and saving resources</li>"
            "</ul>"
        ),
        "results": (
            "<p>Deployed across multiple Lufthansa Group airlines with measurable impact:</p>"
            "<ul>"
            "<li><strong>3-15% increase in ancillary purchases</strong> across different touchpoints and devices</li>"
            "<li><strong>20x API performance gain</strong> enabling real-time recommendations</li>"
            "<li>Destination recommender APIs also optimised for a <strong>2x performance gain</strong></li>"
            "<li>Influenced another team to adopt the centralised API, preventing duplicate development</li>"
            "</ul>"
        ),
        "metrics": json.dumps(
            [
                {"value": "3-15%", "label": "Purchase Uplift"},
                {"value": "20x", "label": "Ancillary API Speedup"},
                {"value": "2x", "label": "Destination API Speedup"},
                {"value": "Multi", "label": "Airline Partners"},
            ]
        ),
    },
    {
        "title": "Generative AI City Recommender",
        "short_description": "First GenAI model for destination scoring & diversity.",
        "description": (
            "Pioneered the first generative AI-based 'categories model' to score city "
            "destinations. The model significantly improved the diversity and relevance "
            "of travel recommendations by combining category embeddings with frequency- "
            "based signals, serving the 95%+ non-logged-in customer base."
        ),
        "technologies": "Python,Generative AI,Azure OpenAI,Pandas,NumPy",
        "category": "genai",
        "year": "2024",
        "client": "Lufthansa Group",
        "featured": True,
        "sort_order": 3,
        "has_case_study": True,
        "challenge": (
            "<p>Over <strong>95% of visitors</strong> to Lufthansa Group websites are non-logged-in users. "
            "Traditional collaborative filtering is impossible due to the cold-start problem. "
            "The existing frequency-table model served generic, popularity-biased recommendations "
            "that lacked diversity and relevance.</p>"
        ),
        "approach": (
            "<p>Pioneered an innovative approach combining generative AI with the existing frequency table:</p>"
            "<ul>"
            "<li><strong>Category Model:</strong> Used generative AI to score city destinations with "
            "nuanced category profiles, creating the first GenAI-based model in the recommendation system</li>"
            "<li><strong>Integration Strategy:</strong> Picked the top categories for each city, then "
            "recommended similar cities based on shared top categories — combining the category model "
            "with the frequency table using an innovative approach</li>"
            "<li><strong>Diversity:</strong> The category-based approach naturally improved recommendation "
            "diversity by surfacing destinations that match user interests rather than just popularity</li>"
            "</ul>"
        ),
        "results": (
            "<p>Transformed destination recommendations for the majority of website visitors:</p>"
            "<ul>"
            "<li>Significantly <strong>improved diversity and relevance</strong> of destination recommendations</li>"
            "<li>Served the <strong>95%+ non-logged-in customer base</strong> that the previous model underserved</li>"
            "<li>First successful application of <strong>generative AI within the recommendation system</strong></li>"
            "<li>Enhanced the previously underperforming frequency table model through improved category integration</li>"
            "</ul>"
        ),
        "metrics": json.dumps(
            [
                {"value": "95%+", "label": "Traffic Served"},
                {"value": "1st", "label": "GenAI in RecSys"},
                {"value": "\u2191", "label": "Recommendation Diversity"},
                {"value": "\u2191", "label": "Relevance vs Frequency Table"},
            ]
        ),
    },
    {
        "title": "AB Testing Framework",
        "short_description": "Comprehensive experimentation pipeline with causal inference.",
        "description": (
            "Led research and development of a comprehensive, generalised AB testing framework. "
            "Includes covariate balance checking, ATE analysis, and a sophisticated CATE framework "
            "with five meta-learners, SHAP-based customer archetype discovery, and automated "
            "dual-reporting (technical and stakeholder)."
        ),
        "technologies": "Python,Causal Inference,SHAP,Meta-Learners,Statistical Testing",
        "category": "recsys",
        "year": "2024",
        "client": "Lufthansa Group",
        "featured": False,
        "sort_order": 4,
    },
    {
        "title": "Human Behavior Simulation",
        "short_description": "Multi-modal AI: voice cloning + 3D avatar + RL agent.",
        "description": (
            "Master's thesis combining three AI modalities: Zero-Shot voice cloning, "
            "3D avatar reconstruction (PIFu), and deep RL agent training (PPO)."
        ),
        "technologies": "Python,TensorFlow,Blender,Unity,C#,PPO",
        "category": "rl cv",
        "year": "2021",
        "client": "Arab International University",
        "featured": False,
        "sort_order": 5,
    },
    {
        "title": "Virtual Patient Simulation",
        "short_description": "Interactive AI patient for medical training scenarios.",
        "description": (
            "Developed an AI-powered 'Virtual Patient' simulation for interactive "
            "clinical training."
        ),
        "technologies": "Python,NLP,SGD,Classification,Flask",
        "category": "nlp",
        "year": "2022",
        "client": "Freelance Client",
        "featured": False,
        "sort_order": 6,
    },
    {
        "title": "Dark Web Auto-Labelling",
        "short_description": "Automated classification of dark web content.",
        "description": (
            "Built an automated system for scraping, labelling, and classifying dark web "
            "content using NLP-based text classification pipelines."
        ),
        "technologies": "Python,Scikit-Learn,BeautifulSoup,Selenium,NLP",
        "category": "nlp",
        "year": "2022",
        "client": "Freelance Client",
        "featured": False,
        "sort_order": 7,
    },
    {
        "title": "Emotion Prediction from Voice",
        "short_description": "Deep learning classifier for vocal emotion detection.",
        "description": (
            "Deep learning model predicting human emotions (calm, happy, sad, angry, fearful, "
            "surprised, disgusted) from audio files using Inception networks on mel-spectrograms."
        ),
        "technologies": "Python,TensorFlow,Keras,Inception,Mel-Spectrogram",
        "category": "cv",
        "year": "2021",
        "client": "Damascus Start-Up",
        "featured": False,
        "sort_order": 8,
    },
    {
        "title": "Arabic Tweets Classifier",
        "short_description": "Sentiment analysis for Arabic social media text.",
        "description": (
            "Kaggle competition for classifying Arabic tweets into positive, negative, and neutral "
            "sentiment classes. Achieved 75.9% accuracy using BERT with extensive Arabic language processing."
        ),
        "technologies": "Python,BERT,Arabic NLP,Kaggle",
        "category": "nlp",
        "year": "2021",
        "client": "Damascus Start-Up",
        "featured": False,
        "sort_order": 9,
    },
    {
        "title": "Forex Forecasting (JPY/CAD)",
        "short_description": "Time-series model for foreign exchange prediction.",
        "description": (
            "Predicting JPY/CAD exchange rates using 20 years of scraped economic data from "
            "multiple websites and Reuters news. Combined macroeconomic features from Japan, "
            "Canada, and the USA with deep neural networks for prediction."
        ),
        "technologies": "Python,TensorFlow,Web Scraping,Reuters NLP,Deep NN",
        "category": "nlp",
        "year": "2020",
        "client": "Damascus Start-Up",
        "featured": False,
        "sort_order": 10,
    },
    {
        "title": "RAG Pipeline with Smart Segmentation",
        "short_description": "Retrieval-Augmented Generation with semantic chunking.",
        "description": (
            "RAG pipeline with smart document segmentation inspired by Anthropic's "
            "research, dynamically chunking documents based on semantic boundaries."
        ),
        "technologies": "Python,LangChain,FAISS,Azure OpenAI",
        "category": "genai",
        "year": "2024",
        "client": "Personal Project",
        "featured": False,
        "sort_order": 11,
    },
    {
        "title": "AI Search & Reasoning Agents",
        "short_description": "Multi-step reasoning agents inspired by OpenAI O-series.",
        "description": (
            "Multi-step reasoning AI agents with source credibility assessment, "
            "chain-of-thought reasoning, and autonomous tool use."
        ),
        "technologies": "Python,LangChain,OpenAI,Tool Use,Agents",
        "category": "genai",
        "year": "2024",
        "client": "Personal Project",
        "featured": False,
        "sort_order": 12,
    },
]


BLOG_POSTS = [
    {
        "title": "The Architecture of Thought: How Neuroscience Is Inspiring the Next Wave of AI Agents",
        "slug": "architecture-of-thought-neuroscience-ai-agents",
        "category": "Neuroscience",
        "tags": "Neuroscience,Agentic AI,Multi-Agent Systems,Prefrontal Cortex,LLM Orchestration",
        "read_time": 12,
        "featured": True,
        "published": True,
        "sort_order": 1,
        "excerpt": (
            "Your prefrontal cortex is the world's most sophisticated AI orchestrator — delegating tasks, "
            "managing working memory, and coordinating specialised brain regions. Recent neuroscience reveals "
            "striking parallels with modern multi-agent AI architectures."
        ),
        "content": "<h2>The Brain's Original Multi-Agent Architecture</h2>\n<p>When I built a <strong>multi-agent voice system</strong> for Lufthansa Group's Data Community Day — a system where an LLM orchestrator delegates tasks to specialised search and data analysis agents — I wasn't just engineering software. I was, unknowingly, replicating one of the brain's oldest design patterns.</p>\n<p>The prefrontal cortex (PFC) doesn't do everything itself. It's an <em>executive coordinator</em> — remarkably similar to the orchestrator agent pattern now dominating AI system design. And recent neuroscience research reveals just how deep this parallel runs.</p>\n<h2>The Prefrontal Cortex as Orchestrator</h2>\n<p>A landmark 2024 study published in <em>Nature Neuroscience</em> by Rigotti et al. demonstrated that prefrontal neurons exhibit <strong>\"mixed selectivity\"</strong> — they respond to complex combinations of task variables rather than single features. This is strikingly similar to how LLM-based orchestrators process multi-dimensional context before deciding which specialist to invoke.</p>\n<p>Here's what most people don't realize: <strong>your brain runs on roughly 20 watts of power</strong> — less than a laptop charger. Yet it coordinates approximately 86 billion neurons across hundreds of specialised regions, maintaining coherent behaviour through what neuroscientists call <em>hierarchical predictive processing</em>.</p>\n<blockquote>\n<p>\"The brain doesn't process information — it <em>predicts</em> it. Every neural circuit is running a generative model of the world, constantly updating its predictions against incoming sensory data.\"</p>\n<p>— Karl Friston, Free Energy Principle</p>\n</blockquote>\n<h2>Surprising Parallel: Attention in Brains and Transformers</h2>\n<p>The transformer architecture's <strong>attention mechanism</strong> — the foundation of every modern LLM — bears a remarkable resemblance to the brain's selective attention system. In 2023, researchers at DeepMind and UCL showed that the mathematical operations underlying multi-head attention are functionally equivalent to what hippocampal place cells do when navigating spatial environments.</p>\n<p>But here's what's truly unexpected: the brain invented something even more sophisticated. <strong>Predictive coding theory</strong> suggests that the cortex operates as a hierarchy of generative models, where each level predicts the activity of the level below and only forwards <em>prediction errors</em>. This is more efficient than attention — it only transmits what's surprising.</p>\n<p>This insight is now influencing next-generation AI architectures. Papers from Anthropic and Google DeepMind in 2025 are exploring \"predictive routing\" mechanisms that could make transformer inference dramatically more efficient by only processing tokens that violate the model's expectations.</p>\n<h2>The Workspace Theory: What Consciousness Teaches AI</h2>\n<p>Cognitive scientist Bernard Baars proposed the <strong>Global Workspace Theory (GWT)</strong> of consciousness in the 1980s — the idea that consciousness emerges from a \"workspace\" where specialised cognitive modules compete for access to broadcast their information globally.</p>\n<p>Sound familiar? It's precisely the architecture of modern multi-agent AI systems:</p>\n<ul>\n<li><strong>Specialised agents</strong> = specialised brain modules (Broca's area for language, fusiform face area for facial recognition, etc.)</li>\n<li><strong>Orchestrator/dispatcher</strong> = the global workspace (prefrontal cortex + thalamus)</li>\n<li><strong>Context window</strong> = working memory (limited to ~4 chunks, just like the 7 plus/minus 2 items in human short-term memory)</li>\n</ul>\n<p>In my work building agentic systems at zeroG, I've found that the most robust agent architectures mirror this neural blueprint: a coordinator that maintains state, specialist agents that process domain-specific queries, and a shared context that accumulates findings — just like the brain's working memory.</p>\n<h2>The Cerebellum: Nature's Pre-Trained Model</h2>\n<p>Here's a fact that shocks most AI researchers: <strong>the cerebellum contains more neurons than the rest of the brain combined</strong> (~69 billion out of ~86 billion). Yet neuroscience has largely ignored it, calling it the \"little brain\" responsible for mere motor coordination.</p>\n<p>Recent research paints a radically different picture. The cerebellum appears to function as a <strong>universal prediction engine</strong> — it builds forward models of everything: motor sequences, language patterns, social expectations, even abstract thought. When you finish someone's sentence, your cerebellum predicted it 300ms before they said it.</p>\n<p>This is essentially what pre-training does for LLMs. The cerebellum is nature's answer to \"How do you build a foundation model?\" — a massive, uniform neural network trained on the statistics of life experience to predict what comes next.</p>\n<h2>From Brains to Systems: Engineering Lessons</h2>\n<p>After years of building AI systems professionally and studying neuroscience as a personal passion, I've identified three principles that emerge from both disciplines:</p>\n<ol>\n<li><strong>Delegation over computation:</strong> The brain doesn't compute everything centrally. Neither should your AI system. Specialise and delegate.</li>\n<li><strong>Prediction over reaction:</strong> The most efficient systems anticipate rather than respond. Build predictive models, not just reactive pipelines.</li>\n<li><strong>Error signals over raw data:</strong> The brain transmits surprises, not observations. Design systems that focus on what's unexpected — it's where the information lives.</li>\n</ol>\n<p>The next frontier in AI isn't just more parameters or bigger context windows. It's learning from the architecture that 600 million years of evolution already optimised — the architecture of thought itself.</p>\n<p><em>This article reflects insights from my research and hands-on experience building multi-agent AI systems at zeroG (Lufthansa Group). The neuroscience references draw from peer-reviewed research published in Nature Neuroscience, Neuron, and Trends in Cognitive Sciences.</em></p>",
        "created_at": datetime(2026, 2, 15),
    },
    {
        "title": "From Chatty Cathy to Autonomous Reasoners: The Agentic AI Revolution",
        "slug": "agentic-ai-revolution-autonomous-reasoners",
        "category": "AI",
        "tags": "Agentic AI,LLM,Autonomous Agents,ReAct,Tool Use,Reasoning",
        "read_time": 10,
        "featured": True,
        "published": True,
        "sort_order": 2,
        "excerpt": (
            "We're witnessing the most fundamental shift in AI since deep learning: "
            "the transition from models that chat to systems that reason, plan, and act. "
            "Here's what's really happening behind the hype — and what I've learned building these systems."
        ),
        "content": "<h2>The Quiet Revolution</h2>\n<p>In 2023, you asked an LLM a question and it answered. In 2024, you asked it to accomplish a goal and it wrote code. In 2025, you described a <em>problem</em> and it assembled a team of agents to solve it autonomously.</p>\n<p>This isn't incremental progress. It's a phase transition. And having built one of these systems live on stage — <strong>a voice-activated multi-agent system for the Lufthansa Group Data Community Day</strong> — I can tell you the gap between \"chatbot\" and \"autonomous agent\" is larger than most people appreciate.</p>\n<h2>What Actually Changed?</h2>\n<p>Three breakthroughs converged to make agentic AI possible:</p>\n<h3>1. Reliable Tool Use</h3>\n<p>The moment LLMs could <strong>reliably call functions</strong> — querying databases, invoking APIs, running code — they stopped being conversationalists and became operators. OpenAI's function calling, Anthropic's tool use, and Google's extensions all shipped within months of each other in 2023-2024.</p>\n<h3>2. Chain-of-Thought Reasoning</h3>\n<p>The publication of <strong>ReAct (Reasoning + Acting)</strong> by Yao et al. showed that interleaving reasoning traces with action steps dramatically improved task completion rates. But here's the underappreciated insight: ReAct works because it externalises the model's \"thinking\" — making its planning process legible and debuggable.</p>\n<p>In my own work, I've found that the quality of an agent system depends less on the model's raw intelligence and more on <strong>the quality of its reasoning scaffolding</strong>. Give a mediocre model great tools and clear reasoning templates, and it will outperform a frontier model with poor scaffolding.</p>\n<h3>3. Multi-Agent Coordination</h3>\n<p>Single agents hit a ceiling quickly. The breakthrough came from <strong>splitting responsibilities</strong> across specialised agents — mirroring how human organisations work.</p>\n<h2>What Most People Get Wrong</h2>\n<p>Having built and deployed agentic systems at enterprise scale, here's what the hype cycle misses:</p>\n<h3>The Reliability Problem Is Not Solved</h3>\n<p>\"Demo-quality\" agent systems fail spectacularly in production. A system that works 90% of the time in a demo fails roughly <strong>every 10th customer interaction</strong>. When I designed the live demo for Data Community Day, I spent 70% of development time on error handling, fallback strategies, and graceful degradation — not on the \"cool\" agent orchestration.</p>\n<h3>Latency Is the Silent Killer</h3>\n<p>Multi-step agent reasoning introduces <strong>compounding latency</strong>. Each LLM call adds 1-3 seconds. A four-step reasoning chain takes 8-12 seconds. The solution isn't faster models — it's better <strong>architecture</strong>: parallel agent execution, speculative tool calling, and aggressive caching.</p>\n<h3>The 95% Problem</h3>\n<p>Here's the number that haunts every agent builder: <strong>95% of your users won't have the data you need to personalise for them</strong>. At Lufthansa Group, 95%+ of website visitors are non-logged-in. Our solution — using generative AI to synthesise \"category profiles\" for destinations — was born from this constraint.</p>\n<h2>Where This Is Going</h2>\n<p>The next two years will see three major developments:</p>\n<ol>\n<li><strong>Agent Operating Systems:</strong> Standardised \"operating systems\" for agents — with process management, memory systems, and inter-agent communication protocols. Model Context Protocol (MCP) is an early example.</li>\n<li><strong>Specialised Agent Hardware:</strong> New silicon optimised for the frequent, small, context-heavy calls that agent systems make.</li>\n<li><strong>Agent-Native Applications:</strong> Applications where the entire UX is built around an autonomous agent that happens to have a human-friendly interface.</li>\n</ol>\n<p>We're not building smarter chatbots. We're building a new kind of software — software that reasons, plans, and acts. <strong>The agent era is the main event.</strong></p>\n<p><em>Based on hands-on experience building production agentic AI systems at zeroG (Lufthansa Group).</em></p>",
        "created_at": datetime(2026, 2, 1),
    },
    {
        "title": "The Neural Canvas: Where Art, Neuroscience, and AI Converge",
        "slug": "neural-canvas-art-neuroscience-ai",
        "category": "Art",
        "tags": "Neuroaesthetics,Generative Art,Neural Style Transfer,Creativity,GANs,Voice Cloning",
        "read_time": 14,
        "featured": True,
        "published": True,
        "sort_order": 3,
        "excerpt": (
            "Your brain's visual cortex uses operations remarkably similar to convolutional neural networks. "
            "Beauty activates the same reward circuits as food and sex. And AI is now creating art that triggers "
            "genuine aesthetic experiences. The convergence of these fields is revealing something profound."
        ),
        "content": "<h2>When Your Brain Looks at Art, It's Running a Neural Network</h2>\n<p>In 2014, neuroscientist Semir Zeki published a finding that would bridge two worlds: when humans experience beauty — whether in visual art, music, or mathematical equations — it activates a specific region of the medial orbito-frontal cortex. The same region. Every time.</p>\n<p>This wasn't just a curious observation. It suggested something radical: <strong>beauty is a computation</strong>, not just a feeling. And if beauty is a computation, then it can — at least in principle — be understood, modelled, and perhaps even generated by artificial systems.</p>\n<h2>The Hidden Mathematics of Visual Perception</h2>\n<p>Here's something that most people don't realize: <strong>the primate visual cortex was the direct inspiration for convolutional neural networks (CNNs)</strong>.</p>\n<p>In 1962, Hubel and Wiesel discovered that neurons in the visual cortex are organised hierarchically:</p>\n<ul>\n<li><strong>V1 (primary visual cortex):</strong> Detects edges and orientations — exactly like the first layers of a CNN</li>\n<li><strong>V2:</strong> Combines edges into textures and simple shapes — like middle CNN layers</li>\n<li><strong>V4:</strong> Processes colour and complex forms — analogous to deeper feature maps</li>\n<li><strong>IT (inferotemporal cortex):</strong> Recognises objects and faces — like the final classification layers</li>\n</ul>\n<p>This isn't a loose analogy. The mathematical operations are <em>functionally identical</em>: spatial convolutions followed by nonlinear activation functions followed by pooling. Evolution discovered deep learning 500 million years before Yann LeCun.</p>\n<h2>Neuroaesthetics: The Science of Why You Stop at a Painting</h2>\n<h3>The Processing Fluency Effect</h3>\n<p>We find images more beautiful when our brains can process them efficiently. This explains why we're drawn to <strong>symmetry, golden ratios, and fractal patterns</strong>. But there's a twist: <em>too much</em> fluency is boring. Peak aesthetic experience occurs at the boundary between order and surprise — <strong>\"optimal complexity.\"</strong></p>\n<h3>The Surprise Paradox</h3>\n<p>The most memorable art violates our expectations while still being interpretable. Neuroimaging studies show that <strong>surprise activates the dopamine system</strong> — the same circuitry involved in learning and reward. Great art is literally teaching us something — reshaping our internal models.</p>\n<h2>My Thesis: Bridging Art, Body, and Machine</h2>\n<p>My master's thesis, <strong>\"Human Behavior Simulation,\"</strong> was an attempt to bridge this convergence directly, combining three modalities:</p>\n<ol>\n<li><strong>Voice Cloning (Zero-Shot Learning):</strong> Synthesising a human voice from just 5-20 seconds of audio — the most personal form of human artistic expression, reproduced through neural networks</li>\n<li><strong>3D Avatar Reconstruction (PIFu):</strong> Generating a fully rigged 3D avatar from a single photograph — art transformed into a three-dimensional digital being</li>\n<li><strong>Deep Reinforcement Learning (PPO):</strong> Teaching the avatar to walk through trial and error — creating an unintentionally beautiful choreography of machine learning</li>\n</ol>\n<h2>GANs: The Brain's Own Generative Model</h2>\n<p>Generative Adversarial Networks mirror a fascinating aspect of brain function. The brain actively <strong>generates predictions</strong> about what it expects to see, then compares against actual input. This is essentially the GAN architecture: a generator (cortical prediction) and a discriminator (error detection).</p>\n<p>When you look at art and it takes a moment to \"resolve,\" you're experiencing this generative process in real-time. The aesthetic pleasure comes from the <em>resolution</em> itself: your brain successfully updating its generative model to accommodate something new.</p>\n<h2>The Future: Computational Creativity</h2>\n<p>For the first time, we have AI systems that can <em>generate</em> aesthetic content, neuroscience tools that can <em>measure</em> aesthetic experience, and mathematical frameworks to <em>model</em> the relationship. The convergence isn't about machines replacing artists — it's about <strong>understanding creativity itself</strong>.</p>\n<p>The neural canvas is being painted from both sides: biology and silicon. And the picture emerging is more beautiful than either side could create alone.</p>\n<p><em>This article draws from research in neuroaesthetics, computational neuroscience, and my experience building multi-modal AI systems including voice cloning, 3D reconstruction, and deep reinforcement learning.</em></p>",
        "created_at": datetime(2026, 1, 15),
    },
    {
        "title": "Recommendation Systems at 30,000 Feet: Engineering Serendipity in Aviation",
        "slug": "recommendation-systems-aviation-engineering-serendipity",
        "category": "AI",
        "tags": "Recommendation Systems,Aviation,Cold Start,AB Testing,Personalisation,Machine Learning",
        "read_time": 11,
        "featured": False,
        "published": True,
        "sort_order": 4,
        "excerpt": (
            "Building recommendation systems for airlines is nothing like Netflix or Spotify. "
            "95% of users are anonymous, purchases are infrequent and high-stakes, and a 'wrong' "
            "recommendation can cost real money. Here's what I learned engineering serendipity in aviation."
        ),
        "content": "<h2>This Is Not Netflix</h2>\n<p>When people think \"recommendation systems,\" they think Netflix suggesting movies or Spotify building playlists. These scenarios share a key advantage: <strong>abundant user data</strong>.</p>\n<p>Now imagine building a recommendation system where:</p>\n<ul>\n<li><strong>95% of your users are completely anonymous</strong></li>\n<li>The average user interacts <strong>2-3 times per year</strong></li>\n<li>A single purchase can cost <strong>hundreds or thousands of euros</strong></li>\n<li>You're serving <strong>5+ different airline brands</strong></li>\n</ul>\n<p>Welcome to airline recommendation systems. This has been my world at zeroG (Lufthansa Group) for the past three years.</p>\n<h2>The Cold Start Problem at Scale</h2>\n<p>For most platforms, cold-start users are 10-20% of traffic. For airlines, it's <strong>95%+</strong>.</p>\n<p>What we CAN use: contextual signals (route, travel dates, cabin class, market, device type), aggregate patterns, and our generative AI city model that scores destinations across interest categories.</p>\n<h2>The Art of Measuring Impact</h2>\n<p>Building the recommendation system was hard. <strong>Proving it worked</strong> was harder. I built an AB testing framework from the ground up handling two different segmentation paradigms — logged-in users (by ID) and non-logged-in users (by market-behaviour clusters).</p>\n<p>The key insight: <strong>statistical significance doesn't equal business significance</strong>. We built automated dual-reporting showing both statistical and business impact per segment. This framework eventually led to the <strong>creation of a new team</strong> dedicated to performance measurement.</p>\n<h2>The 20x Optimisation</h2>\n<p>The biggest improvement wasn't a better model — it was a better <strong>API architecture</strong>. Vectorised scoring, connection pooling, response caching, and lazy loading achieved a <strong>20x performance improvement</strong>. Same model, same accuracy, but now fast enough for real-time use.</p>\n<h2>What Airlines Can Teach Silicon Valley</h2>\n<ol>\n<li><strong>Anonymous users aren't empty — they're just different.</strong> Every interaction carries contextual information.</li>\n<li><strong>Measurement infrastructure > model sophistication.</strong> A mediocre model with great AB testing will outperform a brilliant model you can't evaluate.</li>\n<li><strong>Performance IS product quality.</strong> A 5-second recommendation will never be deployed at the point of maximum impact.</li>\n<li><strong>Cross-partner generalisation is hard.</strong> Culturally-aware, market-specific adaptations matter enormously.</li>\n</ol>\n<p><em>Based on 3+ years building recommendation systems at zeroG (Lufthansa Group).</em></p>",
        "created_at": datetime(2025, 12, 20),
    },
]


SITE_CONFIGS = [
    # ── Hero Section ──
    {
        "key": "hero_label",
        "value": "DATA SCIENTIST &bull; AI ENGINEER",
        "label": "Label / Title Bar",
        "group": "hero",
    },
    {
        "key": "hero_name_line1",
        "value": "MOHAMED",
        "label": "Name Line 1",
        "group": "hero",
    },
    {
        "key": "hero_name_line2",
        "value": "MAA ALBARED",
        "label": "Name Line 2",
        "group": "hero",
    },
    {
        "key": "hero_tagline_word1",
        "value": "Architecting",
        "label": "Tagline Word 1",
        "group": "hero",
    },
    {
        "key": "hero_tagline_word2",
        "value": "Intelligence",
        "label": "Tagline Word 2",
        "group": "hero",
    },
    {
        "key": "hero_subtitle",
        "value": "Where neural networks meet creative intuition – building systems that reason, collaborate, and act.",
        "label": "Subtitle",
        "group": "hero",
    },
    # ── About Section ──
    {
        "key": "about_bio1",
        "value": "Accomplished Data Scientist with over <strong>4 years of experience</strong> specializing in the development and deployment of machine learning and generative AI solutions within the <strong>aviation sector</strong>.",
        "label": "Bio Paragraph 1",
        "group": "about",
    },
    {
        "key": "about_bio2",
        "value": "Proven track record of driving significant business value by architecting <strong>recommendation systems</strong>, optimizing model performance by up to <strong>20x</strong>, and pioneering <strong>AB testing frameworks</strong> from the ground up.",
        "label": "Bio Paragraph 2",
        "group": "about",
    },
    {
        "key": "about_bio3",
        "value": "Recognized as a subject matter expert in <strong>LLM orchestration</strong> and <strong>autonomous agent design</strong>, adept at translating complex AI capabilities into strategic, impactful business outcomes.",
        "label": "Bio Paragraph 3",
        "group": "about",
    },
    {
        "key": "about_years",
        "value": "4",
        "label": "Years of Experience",
        "group": "about",
    },
    {
        "key": "about_projects_count",
        "value": "50+",
        "label": "Projects Delivered",
        "group": "about",
    },
    {
        "key": "about_perf_gains",
        "value": "20",
        "label": "Performance Gains (x)",
        "group": "about",
    },
    # ── Impact Numbers ──
    # (moved to ImpactCard model — see IMPACT_CARDS below)
]


# ═══════════════════════════════════════════════════════════════
# IMPACT CARDS  (Homepage – Impact Numbers Section)
# ═══════════════════════════════════════════════════════════════
IMPACT_CARDS = [
    {
        "icon": "&#9883;",
        "value": "15",
        "prefix": "",
        "suffix": "%",
        "description": "Ancillary purchase lift across airline partners",
        "sort_order": 1,
    },
    {
        "icon": "&#9889;",
        "value": "20",
        "prefix": "",
        "suffix": "x",
        "description": "Recommender API speedup for real-time scoring",
        "sort_order": 2,
    },
    {
        "icon": "&#9992;",
        "value": "6",
        "prefix": "",
        "suffix": "+",
        "description": "Airlines served with personalized recommendations",
        "sort_order": 3,
    },
    {
        "icon": "&#9733;",
        "value": "2",
        "prefix": "",
        "suffix": "x",
        "description": "Keynote presenter at the biggest LHG data event",
        "sort_order": 4,
    },
]


# ═══════════════════════════════════════════════════════════════
# SKILL CLUSTERS  (Homepage – Capabilities Section)
# ═══════════════════════════════════════════════════════════════
SKILL_CLUSTERS = [
    {
        "icon": "&#129302;",
        "title": "Generative & Agentic AI",
        "tags": "LLM Orchestration, Multi-Agent Systems, Prompt Engineering, RAG Pipelines, Fine-Tuning, LangChain/LangGraph, Semantic Kernel",
        "sort_order": 1,
    },
    {
        "icon": "&#129504;",
        "title": "ML & Data Science",
        "tags": "Recommendation Systems, NLP/NLU, Classification, Regression, Feature Engineering, A/B Testing, XGBoost, Deep Learning",
        "sort_order": 2,
    },
    {
        "icon": "&#128187;",
        "title": "Tech Stack",
        "tags": "Python, SQL, Flask, FastAPI, TensorFlow, PyTorch, scikit-learn, Pandas, NumPy, Git, REST APIs",
        "sort_order": 3,
    },
    {
        "icon": "&#9729;",
        "title": "Cloud & MLOps",
        "tags": "Azure ML, AWS (S3, Lambda), Docker, CI/CD, MLflow, Weights & Biases, Databricks, Airflow",
        "sort_order": 4,
    },
]


# ═══════════════════════════════════════════════════════════════
# LANGUAGES  (Homepage – Languages mini-section)
# ═══════════════════════════════════════════════════════════════
LANGUAGE_ITEMS = [
    {"name": "Arabic", "level": "Native", "sort_order": 1},
    {"name": "English", "level": "C1-C2", "sort_order": 2},
    {"name": "German", "level": "A2", "sort_order": 3},
]


def seed():
    with app.app_context():
        db.create_all()

        # Skip seeding if data already exists (preserves admin-added content)
        if Project.query.first() is not None:
            print("Database already has data — skipping seed.")
            print("To force re-seed, run:  python seed.py --force")
            return

        for exp_data in EXPERIENCES:
            db.session.add(Experience(**exp_data))

        for proj_data in PROJECTS:
            db.session.add(Project(**proj_data))

        for post_data in BLOG_POSTS:
            db.session.add(BlogPost(**post_data))

        for cfg_data in SITE_CONFIGS:
            db.session.add(SiteConfig(**cfg_data))

        for card_data in IMPACT_CARDS:
            db.session.add(ImpactCard(**card_data))

        for cluster_data in SKILL_CLUSTERS:
            db.session.add(SkillCluster(**cluster_data))

        for lang_data in LANGUAGE_ITEMS:
            db.session.add(LanguageItem(**lang_data))

        db.session.commit()
        print(
            f"Seeded {len(EXPERIENCES)} experiences, "
            f"{len(PROJECTS)} projects, "
            f"{len(BLOG_POSTS)} blog posts, "
            f"{len(SITE_CONFIGS)} site config entries, "
            f"{len(IMPACT_CARDS)} impact cards, "
            f"{len(SKILL_CLUSTERS)} skill clusters, and "
            f"{len(LANGUAGE_ITEMS)} languages."
        )


if __name__ == "__main__":
    import sys

    if "--force" in sys.argv:
        with app.app_context():
            db.drop_all()
            db.create_all()
            print("Force re-seed: all tables dropped and recreated.")
    seed()
