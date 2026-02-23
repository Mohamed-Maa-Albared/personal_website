"""
Seed script — Populate the database with Mohamed's projects, experience, blog posts, and case studies.
Run with:  python seed.py
"""

import json
import os
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
                "Keynote on Agentic AI with live multi-agent system demo at Data Community Day",
                "Pioneered first generative AI 'categories model' for city destination scoring",
                "Engineered ancillary recommender, driving 3-15% purchase increase across airlines",
                "Re-factored recommender APIs for up to 20x performance gain",
                "Built AB testing pipeline from scratch for rigorous model validation",
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
                "'Virtual Patient' simulation for interactive medical training",
                "Automated Dark Web Auto-Labelling & Classification system",
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
                "Algorithms & Data Structures lab instructor",
                "Delivered Reinforcement Learning workshop (Smart Tech Institute, 2021)",
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
            "Owned the full data science pipeline from web scraping and cleaning "
            "to modelling and deployment of predictive systems."
        ),
        "highlights": json.dumps(
            [
                "Foreign Exchange Forecasting (JPY/CAD): time-series model",
                "Emotion Prediction from Voice: deep learning classifier",
                "Arabic Tweets Classifier: NLP sentiment analysis",
            ]
        ),
        "sort_order": 4,
    },
    {
        "role": "BSc Informatics Engineering, AI Major",
        "company": "Arab International University",
        "location": "Damascus, Syria",
        "date_range": "Sep 2015 – Mar 2021",
        "description": (
            "Thesis: Human Behavior Simulation. A multi-modal AI system combining "
            "voice cloning, 3D avatar reconstruction, and deep RL agent training."
        ),
        "highlights": json.dumps(
            [
                "Voice Cloning via Zero-Shot Learning from 5-20s audio samples",
                "3D Avatar Reconstruction using Facebook's PIFu from a single image",
                "RL Agent trained to walk in Blender/Unity via PPO",
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
            "Includes covariate balance checking, ATE analysis, and a CATE framework "
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
        "value": "Where neural networks meet creative intuition. Building systems that reason, collaborate, and act.",
        "label": "Subtitle",
        "group": "hero",
    },
    # ── About Section ──
    {
        "key": "about_bio1",
        "value": "Data Scientist with <strong>4+ years of experience</strong> building and deploying machine learning and generative AI solutions in the <strong>aviation sector</strong>.",
        "label": "Bio Paragraph 1",
        "group": "about",
    },
    {
        "key": "about_bio2",
        "value": "I build <strong>recommendation systems</strong> that move the needle (3-15% purchase lift), optimize ML pipelines for up to <strong>20x</strong> faster response, and design <strong>AB testing frameworks</strong> from scratch.",
        "label": "Bio Paragraph 2",
        "group": "about",
    },
    {
        "key": "about_bio3",
        "value": "Go-to person for <strong>LLM orchestration</strong> and <strong>autonomous agent design</strong> at zeroG, turning cutting-edge AI research into systems that actually ship.",
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
        "value": "10",
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
