--
-- PostgreSQL database dump
--

\restrict g78XSuhZZ2Cduo3Yk876t8nm6Hh4jA7IEUdgF2AfsEinT0OmxWp7qbdYJ31PMmp

-- Dumped from database version 18.1 (Debian 18.1-1.pgdg12+2)
-- Dumped by pg_dump version 18.3 (Ubuntu 18.3-1.pgdg24.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

-- *not* creating schema, since initdb creates it


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: blog_posts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.blog_posts (
    id integer NOT NULL,
    title character varying(300) NOT NULL,
    slug character varying(300) NOT NULL,
    excerpt character varying(500),
    content text NOT NULL,
    cover_image character varying(500),
    category character varying(100),
    tags character varying(500),
    read_time integer,
    published boolean,
    featured boolean,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    sort_order integer
);


--
-- Name: blog_posts_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.blog_posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: blog_posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.blog_posts_id_seq OWNED BY public.blog_posts.id;


--
-- Name: experiences; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.experiences (
    id integer NOT NULL,
    role character varying(200) NOT NULL,
    company character varying(200) NOT NULL,
    location character varying(200),
    date_range character varying(100) NOT NULL,
    description text,
    highlights text,
    sort_order integer
);


--
-- Name: experiences_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.experiences_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: experiences_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.experiences_id_seq OWNED BY public.experiences.id;


--
-- Name: impact_cards; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.impact_cards (
    id integer NOT NULL,
    icon character varying(50) NOT NULL,
    value character varying(50) NOT NULL,
    prefix character varying(20),
    suffix character varying(20),
    description character varying(300) NOT NULL,
    sort_order integer
);


--
-- Name: impact_cards_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.impact_cards_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: impact_cards_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.impact_cards_id_seq OWNED BY public.impact_cards.id;


--
-- Name: language_items; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.language_items (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    level character varying(50) NOT NULL,
    sort_order integer
);


--
-- Name: language_items_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.language_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: language_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.language_items_id_seq OWNED BY public.language_items.id;


--
-- Name: messages; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.messages (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(120) NOT NULL,
    subject character varying(200) NOT NULL,
    message text NOT NULL,
    created_at timestamp without time zone NOT NULL,
    is_read boolean
);


--
-- Name: messages_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.messages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: messages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.messages_id_seq OWNED BY public.messages.id;


--
-- Name: page_visits; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.page_visits (
    id integer NOT NULL,
    path character varying(500) NOT NULL,
    referrer character varying(500),
    user_agent character varying(500),
    ip_hash character varying(64),
    country character varying(100),
    visited_at timestamp without time zone NOT NULL
);


--
-- Name: page_visits_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.page_visits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: page_visits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.page_visits_id_seq OWNED BY public.page_visits.id;


--
-- Name: projects; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects (
    id integer NOT NULL,
    title character varying(200) NOT NULL,
    description text NOT NULL,
    short_description character varying(300),
    image_url character varying(500),
    demo_url character varying(500),
    github_url character varying(500),
    technologies character varying(500),
    category character varying(100),
    year character varying(20),
    client character varying(200),
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    featured boolean,
    case_study text,
    metrics text,
    challenge text,
    approach text,
    results text,
    has_case_study boolean,
    sort_order integer
);


--
-- Name: projects_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.projects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: projects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.projects_id_seq OWNED BY public.projects.id;


--
-- Name: site_config; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.site_config (
    id integer NOT NULL,
    key character varying(100) NOT NULL,
    value text NOT NULL,
    label character varying(200),
    "group" character varying(50)
);


--
-- Name: site_config_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.site_config_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: site_config_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.site_config_id_seq OWNED BY public.site_config.id;


--
-- Name: skill_clusters; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.skill_clusters (
    id integer NOT NULL,
    icon character varying(50) NOT NULL,
    title character varying(200) NOT NULL,
    tags text NOT NULL,
    sort_order integer
);


--
-- Name: skill_clusters_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.skill_clusters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: skill_clusters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.skill_clusters_id_seq OWNED BY public.skill_clusters.id;


--
-- Name: blog_posts id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_posts ALTER COLUMN id SET DEFAULT nextval('public.blog_posts_id_seq'::regclass);


--
-- Name: experiences id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.experiences ALTER COLUMN id SET DEFAULT nextval('public.experiences_id_seq'::regclass);


--
-- Name: impact_cards id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.impact_cards ALTER COLUMN id SET DEFAULT nextval('public.impact_cards_id_seq'::regclass);


--
-- Name: language_items id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.language_items ALTER COLUMN id SET DEFAULT nextval('public.language_items_id_seq'::regclass);


--
-- Name: messages id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.messages ALTER COLUMN id SET DEFAULT nextval('public.messages_id_seq'::regclass);


--
-- Name: page_visits id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.page_visits ALTER COLUMN id SET DEFAULT nextval('public.page_visits_id_seq'::regclass);


--
-- Name: projects id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects ALTER COLUMN id SET DEFAULT nextval('public.projects_id_seq'::regclass);


--
-- Name: site_config id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.site_config ALTER COLUMN id SET DEFAULT nextval('public.site_config_id_seq'::regclass);


--
-- Name: skill_clusters id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.skill_clusters ALTER COLUMN id SET DEFAULT nextval('public.skill_clusters_id_seq'::regclass);


--
-- Data for Name: blog_posts; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.blog_posts (id, title, slug, excerpt, content, cover_image, category, tags, read_time, published, featured, created_at, updated_at, sort_order) FROM stdin;
1	The Architecture of Thought: How Neuroscience Is Inspiring the Next Wave of AI Agents	architecture-of-thought-neuroscience-ai-agents	Your prefrontal cortex is the world's most sophisticated AI orchestrator — delegating tasks, managing working memory, and coordinating specialised brain regions. Recent neuroscience reveals striking parallels with modern multi-agent AI architectures.	<h2>The Brain's Original Multi-Agent Architecture</h2>\n<p>When I built a <strong>multi-agent voice system</strong> for Lufthansa Group's Data Community Day — a system where an LLM orchestrator delegates tasks to specialised search and data analysis agents — I wasn't just engineering software. I was, unknowingly, replicating one of the brain's oldest design patterns.</p>\n<p>The prefrontal cortex (PFC) doesn't do everything itself. It's an <em>executive coordinator</em> — remarkably similar to the orchestrator agent pattern now dominating AI system design. And recent neuroscience research reveals just how deep this parallel runs.</p>\n<h2>The Prefrontal Cortex as Orchestrator</h2>\n<p>A landmark 2024 study published in <em>Nature Neuroscience</em> by Rigotti et al. demonstrated that prefrontal neurons exhibit <strong>"mixed selectivity"</strong> — they respond to complex combinations of task variables rather than single features. This is strikingly similar to how LLM-based orchestrators process multi-dimensional context before deciding which specialist to invoke.</p>\n<p>Here's what most people don't realize: <strong>your brain runs on roughly 20 watts of power</strong> — less than a laptop charger. Yet it coordinates approximately 86 billion neurons across hundreds of specialised regions, maintaining coherent behaviour through what neuroscientists call <em>hierarchical predictive processing</em>.</p>\n<blockquote>\n<p>"The brain doesn't process information — it <em>predicts</em> it. Every neural circuit is running a generative model of the world, constantly updating its predictions against incoming sensory data."</p>\n<p>— Karl Friston, Free Energy Principle</p>\n</blockquote>\n<h2>Surprising Parallel: Attention in Brains and Transformers</h2>\n<p>The transformer architecture's <strong>attention mechanism</strong> — the foundation of every modern LLM — bears a remarkable resemblance to the brain's selective attention system. In 2023, researchers at DeepMind and UCL showed that the mathematical operations underlying multi-head attention are functionally equivalent to what hippocampal place cells do when navigating spatial environments.</p>\n<p>But here's what's truly unexpected: the brain invented something even more sophisticated. <strong>Predictive coding theory</strong> suggests that the cortex operates as a hierarchy of generative models, where each level predicts the activity of the level below and only forwards <em>prediction errors</em>. This is more efficient than attention — it only transmits what's surprising.</p>\n<p>This insight is now influencing next-generation AI architectures. Papers from Anthropic and Google DeepMind in 2025 are exploring "predictive routing" mechanisms that could make transformer inference dramatically more efficient by only processing tokens that violate the model's expectations.</p>\n<h2>The Workspace Theory: What Consciousness Teaches AI</h2>\n<p>Cognitive scientist Bernard Baars proposed the <strong>Global Workspace Theory (GWT)</strong> of consciousness in the 1980s — the idea that consciousness emerges from a "workspace" where specialised cognitive modules compete for access to broadcast their information globally.</p>\n<p>Sound familiar? It's precisely the architecture of modern multi-agent AI systems:</p>\n<ul>\n<li><strong>Specialised agents</strong> = specialised brain modules (Broca's area for language, fusiform face area for facial recognition, etc.)</li>\n<li><strong>Orchestrator/dispatcher</strong> = the global workspace (prefrontal cortex + thalamus)</li>\n<li><strong>Context window</strong> = working memory (limited to ~4 chunks, just like the 7 plus/minus 2 items in human short-term memory)</li>\n</ul>\n<p>In my work building agentic systems at zeroG, I've found that the most robust agent architectures mirror this neural blueprint: a coordinator that maintains state, specialist agents that process domain-specific queries, and a shared context that accumulates findings — just like the brain's working memory.</p>\n<h2>The Cerebellum: Nature's Pre-Trained Model</h2>\n<p>Here's a fact that shocks most AI researchers: <strong>the cerebellum contains more neurons than the rest of the brain combined</strong> (~69 billion out of ~86 billion). Yet neuroscience has largely ignored it, calling it the "little brain" responsible for mere motor coordination.</p>\n<p>Recent research paints a radically different picture. The cerebellum appears to function as a <strong>universal prediction engine</strong> — it builds forward models of everything: motor sequences, language patterns, social expectations, even abstract thought. When you finish someone's sentence, your cerebellum predicted it 300ms before they said it.</p>\n<p>This is essentially what pre-training does for LLMs. The cerebellum is nature's answer to "How do you build a foundation model?" — a massive, uniform neural network trained on the statistics of life experience to predict what comes next.</p>\n<h2>From Brains to Systems: Engineering Lessons</h2>\n<p>After years of building AI systems professionally and studying neuroscience as a personal passion, I've identified three principles that emerge from both disciplines:</p>\n<ol>\n<li><strong>Delegation over computation:</strong> The brain doesn't compute everything centrally. Neither should your AI system. Specialise and delegate.</li>\n<li><strong>Prediction over reaction:</strong> The most efficient systems anticipate rather than respond. Build predictive models, not just reactive pipelines.</li>\n<li><strong>Error signals over raw data:</strong> The brain transmits surprises, not observations. Design systems that focus on what's unexpected — it's where the information lives.</li>\n</ol>\n<p>The next frontier in AI isn't just more parameters or bigger context windows. It's learning from the architecture that 600 million years of evolution already optimised — the architecture of thought itself.</p>\n<p><em>This article reflects insights from my research and hands-on experience building multi-agent AI systems at zeroG (Lufthansa Group). The neuroscience references draw from peer-reviewed research published in Nature Neuroscience, Neuron, and Trends in Cognitive Sciences.</em></p>	\N	Neuroscience	Neuroscience,Agentic AI,Multi-Agent Systems,Prefrontal Cortex,LLM Orchestration	12	t	t	2026-02-15 00:00:00	2026-02-23 11:56:27.701537	1
2	From Chatty Cathy to Autonomous Reasoners: The Agentic AI Revolution	agentic-ai-revolution-autonomous-reasoners	We're witnessing the most fundamental shift in AI since deep learning: the transition from models that chat to systems that reason, plan, and act. Here's what's really happening behind the hype — and what I've learned building these systems.	<h2>The Quiet Revolution</h2>\n<p>In 2023, you asked an LLM a question and it answered. In 2024, you asked it to accomplish a goal and it wrote code. In 2025, you described a <em>problem</em> and it assembled a team of agents to solve it autonomously.</p>\n<p>This isn't incremental progress. It's a phase transition. And having built one of these systems live on stage — <strong>a voice-activated multi-agent system for the Lufthansa Group Data Community Day</strong> — I can tell you the gap between "chatbot" and "autonomous agent" is larger than most people appreciate.</p>\n<h2>What Actually Changed?</h2>\n<p>Three breakthroughs converged to make agentic AI possible:</p>\n<h3>1. Reliable Tool Use</h3>\n<p>The moment LLMs could <strong>reliably call functions</strong> — querying databases, invoking APIs, running code — they stopped being conversationalists and became operators. OpenAI's function calling, Anthropic's tool use, and Google's extensions all shipped within months of each other in 2023-2024.</p>\n<h3>2. Chain-of-Thought Reasoning</h3>\n<p>The publication of <strong>ReAct (Reasoning + Acting)</strong> by Yao et al. showed that interleaving reasoning traces with action steps dramatically improved task completion rates. But here's the underappreciated insight: ReAct works because it externalises the model's "thinking" — making its planning process legible and debuggable.</p>\n<p>In my own work, I've found that the quality of an agent system depends less on the model's raw intelligence and more on <strong>the quality of its reasoning scaffolding</strong>. Give a mediocre model great tools and clear reasoning templates, and it will outperform a frontier model with poor scaffolding.</p>\n<h3>3. Multi-Agent Coordination</h3>\n<p>Single agents hit a ceiling quickly. The breakthrough came from <strong>splitting responsibilities</strong> across specialised agents — mirroring how human organisations work.</p>\n<h2>What Most People Get Wrong</h2>\n<p>Having built and deployed agentic systems at enterprise scale, here's what the hype cycle misses:</p>\n<h3>The Reliability Problem Is Not Solved</h3>\n<p>"Demo-quality" agent systems fail spectacularly in production. A system that works 90% of the time in a demo fails roughly <strong>every 10th customer interaction</strong>. When I designed the live demo for Data Community Day, I spent 70% of development time on error handling, fallback strategies, and graceful degradation — not on the "cool" agent orchestration.</p>\n<h3>Latency Is the Silent Killer</h3>\n<p>Multi-step agent reasoning introduces <strong>compounding latency</strong>. Each LLM call adds 1-3 seconds. A four-step reasoning chain takes 8-12 seconds. The solution isn't faster models — it's better <strong>architecture</strong>: parallel agent execution, speculative tool calling, and aggressive caching.</p>\n<h3>The 95% Problem</h3>\n<p>Here's the number that haunts every agent builder: <strong>95% of your users won't have the data you need to personalise for them</strong>. At Lufthansa Group, 95%+ of website visitors are non-logged-in. Our solution — using generative AI to synthesise "category profiles" for destinations — was born from this constraint.</p>\n<h2>Where This Is Going</h2>\n<p>The next two years will see three major developments:</p>\n<ol>\n<li><strong>Agent Operating Systems:</strong> Standardised "operating systems" for agents — with process management, memory systems, and inter-agent communication protocols. Model Context Protocol (MCP) is an early example.</li>\n<li><strong>Specialised Agent Hardware:</strong> New silicon optimised for the frequent, small, context-heavy calls that agent systems make.</li>\n<li><strong>Agent-Native Applications:</strong> Applications where the entire UX is built around an autonomous agent that happens to have a human-friendly interface.</li>\n</ol>\n<p>We're not building smarter chatbots. We're building a new kind of software — software that reasons, plans, and acts. <strong>The agent era is the main event.</strong></p>\n<p><em>Based on hands-on experience building production agentic AI systems at zeroG (Lufthansa Group).</em></p>	\N	AI	Agentic AI,LLM,Autonomous Agents,ReAct,Tool Use,Reasoning	10	t	t	2026-02-01 00:00:00	2026-02-23 11:56:27.701543	2
3	The Neural Canvas: Where Art, Neuroscience, and AI Converge	neural-canvas-art-neuroscience-ai	Your brain's visual cortex uses operations remarkably similar to convolutional neural networks. Beauty activates the same reward circuits as food and sex. And AI is now creating art that triggers genuine aesthetic experiences. The convergence of these fields is revealing something profound.	<h2>When Your Brain Looks at Art, It's Running a Neural Network</h2>\n<p>In 2014, neuroscientist Semir Zeki published a finding that would bridge two worlds: when humans experience beauty — whether in visual art, music, or mathematical equations — it activates a specific region of the medial orbito-frontal cortex. The same region. Every time.</p>\n<p>This wasn't just a curious observation. It suggested something radical: <strong>beauty is a computation</strong>, not just a feeling. And if beauty is a computation, then it can — at least in principle — be understood, modelled, and perhaps even generated by artificial systems.</p>\n<h2>The Hidden Mathematics of Visual Perception</h2>\n<p>Here's something that most people don't realize: <strong>the primate visual cortex was the direct inspiration for convolutional neural networks (CNNs)</strong>.</p>\n<p>In 1962, Hubel and Wiesel discovered that neurons in the visual cortex are organised hierarchically:</p>\n<ul>\n<li><strong>V1 (primary visual cortex):</strong> Detects edges and orientations — exactly like the first layers of a CNN</li>\n<li><strong>V2:</strong> Combines edges into textures and simple shapes — like middle CNN layers</li>\n<li><strong>V4:</strong> Processes colour and complex forms — analogous to deeper feature maps</li>\n<li><strong>IT (inferotemporal cortex):</strong> Recognises objects and faces — like the final classification layers</li>\n</ul>\n<p>This isn't a loose analogy. The mathematical operations are <em>functionally identical</em>: spatial convolutions followed by nonlinear activation functions followed by pooling. Evolution discovered deep learning 500 million years before Yann LeCun.</p>\n<h2>Neuroaesthetics: The Science of Why You Stop at a Painting</h2>\n<h3>The Processing Fluency Effect</h3>\n<p>We find images more beautiful when our brains can process them efficiently. This explains why we're drawn to <strong>symmetry, golden ratios, and fractal patterns</strong>. But there's a twist: <em>too much</em> fluency is boring. Peak aesthetic experience occurs at the boundary between order and surprise — <strong>"optimal complexity."</strong></p>\n<h3>The Surprise Paradox</h3>\n<p>The most memorable art violates our expectations while still being interpretable. Neuroimaging studies show that <strong>surprise activates the dopamine system</strong> — the same circuitry involved in learning and reward. Great art is literally teaching us something — reshaping our internal models.</p>\n<h2>My Thesis: Bridging Art, Body, and Machine</h2>\n<p>My master's thesis, <strong>"Human Behavior Simulation,"</strong> was an attempt to bridge this convergence directly, combining three modalities:</p>\n<ol>\n<li><strong>Voice Cloning (Zero-Shot Learning):</strong> Synthesising a human voice from just 5-20 seconds of audio — the most personal form of human artistic expression, reproduced through neural networks</li>\n<li><strong>3D Avatar Reconstruction (PIFu):</strong> Generating a fully rigged 3D avatar from a single photograph — art transformed into a three-dimensional digital being</li>\n<li><strong>Deep Reinforcement Learning (PPO):</strong> Teaching the avatar to walk through trial and error — creating an unintentionally beautiful choreography of machine learning</li>\n</ol>\n<h2>GANs: The Brain's Own Generative Model</h2>\n<p>Generative Adversarial Networks mirror a fascinating aspect of brain function. The brain actively <strong>generates predictions</strong> about what it expects to see, then compares against actual input. This is essentially the GAN architecture: a generator (cortical prediction) and a discriminator (error detection).</p>\n<p>When you look at art and it takes a moment to "resolve," you're experiencing this generative process in real-time. The aesthetic pleasure comes from the <em>resolution</em> itself: your brain successfully updating its generative model to accommodate something new.</p>\n<h2>The Future: Computational Creativity</h2>\n<p>For the first time, we have AI systems that can <em>generate</em> aesthetic content, neuroscience tools that can <em>measure</em> aesthetic experience, and mathematical frameworks to <em>model</em> the relationship. The convergence isn't about machines replacing artists — it's about <strong>understanding creativity itself</strong>.</p>\n<p>The neural canvas is being painted from both sides: biology and silicon. And the picture emerging is more beautiful than either side could create alone.</p>\n<p><em>This article draws from research in neuroaesthetics, computational neuroscience, and my experience building multi-modal AI systems including voice cloning, 3D reconstruction, and deep reinforcement learning.</em></p>	\N	Art	Neuroaesthetics,Generative Art,Neural Style Transfer,Creativity,GANs,Voice Cloning	14	t	t	2026-01-15 00:00:00	2026-02-23 11:56:27.701545	3
4	Recommendation Systems at 30,000 Feet: Engineering Serendipity in Aviation	recommendation-systems-aviation-engineering-serendipity	Building recommendation systems for airlines is nothing like Netflix or Spotify. 95% of users are anonymous, purchases are infrequent and high-stakes, and a 'wrong' recommendation can cost real money. Here's what I learned engineering serendipity in aviation.	<h2>This Is Not Netflix</h2>\n<p>When people think "recommendation systems," they think Netflix suggesting movies or Spotify building playlists. These scenarios share a key advantage: <strong>abundant user data</strong>.</p>\n<p>Now imagine building a recommendation system where:</p>\n<ul>\n<li><strong>95% of your users are completely anonymous</strong></li>\n<li>The average user interacts <strong>2-3 times per year</strong></li>\n<li>A single purchase can cost <strong>hundreds or thousands of euros</strong></li>\n<li>You're serving <strong>5+ different airline brands</strong></li>\n</ul>\n<p>Welcome to airline recommendation systems. This has been my world at zeroG (Lufthansa Group) for the past three years.</p>\n<h2>The Cold Start Problem at Scale</h2>\n<p>For most platforms, cold-start users are 10-20% of traffic. For airlines, it's <strong>95%+</strong>.</p>\n<p>What we CAN use: contextual signals (route, travel dates, cabin class, market, device type), aggregate patterns, and our generative AI city model that scores destinations across interest categories.</p>\n<h2>The Art of Measuring Impact</h2>\n<p>Building the recommendation system was hard. <strong>Proving it worked</strong> was harder. I built an AB testing framework from the ground up handling two different segmentation paradigms — logged-in users (by ID) and non-logged-in users (by market-behaviour clusters).</p>\n<p>The key insight: <strong>statistical significance doesn't equal business significance</strong>. We built automated dual-reporting showing both statistical and business impact per segment. This framework eventually led to the <strong>creation of a new team</strong> dedicated to performance measurement.</p>\n<h2>The 20x Optimisation</h2>\n<p>The biggest improvement wasn't a better model — it was a better <strong>API architecture</strong>. Vectorised scoring, connection pooling, response caching, and lazy loading achieved a <strong>20x performance improvement</strong>. Same model, same accuracy, but now fast enough for real-time use.</p>\n<h2>What Airlines Can Teach Silicon Valley</h2>\n<ol>\n<li><strong>Anonymous users aren't empty — they're just different.</strong> Every interaction carries contextual information.</li>\n<li><strong>Measurement infrastructure > model sophistication.</strong> A mediocre model with great AB testing will outperform a brilliant model you can't evaluate.</li>\n<li><strong>Performance IS product quality.</strong> A 5-second recommendation will never be deployed at the point of maximum impact.</li>\n<li><strong>Cross-partner generalisation is hard.</strong> Culturally-aware, market-specific adaptations matter enormously.</li>\n</ol>\n<p><em>Based on 3+ years building recommendation systems at zeroG (Lufthansa Group).</em></p>	\N	AI	Recommendation Systems,Aviation,Cold Start,AB Testing,Personalisation,Machine Learning	11	t	f	2025-12-20 00:00:00	2026-02-23 11:56:27.701546	4
\.


--
-- Data for Name: experiences; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.experiences (id, role, company, location, date_range, description, highlights, sort_order) FROM stdin;
3	Engineering Lecturer (Part-Time)	Arab International University	Damascus, Syria	Feb 2022 — Jun 2022	Instructed undergraduate students in Algorithms &amp; Data Structures. Developed curriculum, projects, and assessments.	["<span class=\\"accent-hl\\">Algorithms &amp; Data Structures</span> lab instructor", "Delivered <span class=\\"accent-hl\\">Reinforcement Learning workshop</span> (Smart Tech Institute, 2021)"]	3
4	Data Scientist	Damascus-based Start-Up	Damascus, Syria	Apr 2020 — Jun 2021	Owned the full data science pipeline — from web scraping and cleaning to modelling and deployment of predictive systems.	["<span class=\\"accent-hl\\">Foreign Exchange Forecasting</span> (JPY/CAD) \\u2014 time-series model", "<span class=\\"accent-hl\\">Emotion Prediction from Voice</span> \\u2014 deep learning classifier", "<span class=\\"accent-hl\\">Arabic Tweets Classifier</span> \\u2014 NLP sentiment analysis"]	4
5	BSc Informatics Engineering — AI Major	Arab International University	Damascus, Syria	Sep 2015 — Mar 2021	Thesis: Human Behavior Simulation — a multi-modal AI system combining voice cloning, 3D avatar reconstruction, and deep RL agent training.	["<span class=\\"accent-hl\\">Voice Cloning </span>via Zero-Shot Learning from 5-20s audio samples", "<span class=\\"accent-hl\\">3D Avatar Reconstruction</span> using Facebook's PIFu from a single image", "<span class=\\"accent-hl\\">RL Agent </span>trained to walk in Unity via PPO"]	5
2	AI Engineer	Freelance	Remote	Apr 2021 — Oct 2022	Delivered end-to-end AI solutions for diverse clients, managing every stage from scoping to deployment and maintenance.	["<span class=\\"accent-hl\\">'Virtual Patient'</span> simulation for interactive medical training", "Automated <span class=\\"accent-hl\\">Dark Web Auto-Labelling &amp; Classification</span> system"]	2
1	Data Scientist	zeroG – AI in Aviation (Lufthansa Group)	Frankfurt, Germany	Dec 2022 — Present	Lead the innovation, design, and implementation of advanced AI systems to drive customer engagement and strategic business initiatives. Serve as a key resource for Generative and Agentic AI.	["<span class=\\"accent-hl\\">Keynote on Agentic AI</span> with live multi-agent system demo at Data Community Day", "Pioneered first <span class=\\"accent-hl\\">g</span><span class=\\"accent-hl\\">enerative AI 'categories model' </span>for city destination scoring", "Engineered <span class=\\"accent-hl\\">ancillary recommender&nbsp;</span><span>driving<span class=\\"Apple-converted-space\\">&nbsp;</span></span><span><span class=\\"accent-hl\\">3-15% purchase increase</span></span><span><span class=\\"Apple-converted-space\\">&nbsp;</span>across airlines</span>", "Optimised recommender APIs for up to <span class=\\"accent-hl\\">20x performance gain</span>", "Built <span class=\\"accent-hl\\">comprehensive AB testing pipeline</span> from scratch for rigorous model validation"]	1
\.


--
-- Data for Name: impact_cards; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.impact_cards (id, icon, value, prefix, suffix, description, sort_order) FROM stdin;
3	&#9992;	6		+	Airlines served with personalized recommendations	3
1	&#9883;	15		%	Ancillary purchase lift across airline partners	1
2	&#9889;	20		x	Recommender API speedup for real-time scoring	2
4	&#9733;	2			Keynote presenter at the biggest LHG data event	4
\.


--
-- Data for Name: language_items; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.language_items (id, name, level, sort_order) FROM stdin;
1	Arabic	Native	1
2	English	C1-C2	2
3	German	A2	3
\.


--
-- Data for Name: messages; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.messages (id, name, email, subject, message, created_at, is_read) FROM stdin;
\.


--
-- Data for Name: page_visits; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.page_visits (id, path, referrer, user_agent, ip_hash, country, visited_at) FROM stdin;
1	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-23 11:57:47.955363
2	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 11:59:50.631439
3	/privacy	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 12:00:15.99511
4	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-23 12:16:55.646869
5	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 12:36:56.378771
6	/blog	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 12:37:08.43186
7	/blog/neural-palette-ai-neuroscience-art-convergence	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 12:37:19.784049
8	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 12:40:46.253962
9	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 12:42:37.574606
10	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 12:43:53.589398
11	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 12:44:23.58249
12	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-23 12:52:51.583797
13	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 13:02:05.291659
14	/blog	https://mohamed-maa-albared-portfolio.onrender.com/blog/neural-palette-ai-neuroscience-art-convergence	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 13:02:12.369944
15	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 13:02:43.211038
16	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-23 13:43:06.646358
17	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-23 13:49:02.590808
18	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 13:49:20.761842
19	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 14:09:34.866022
20	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 14:16:29.487917
21	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 14:37:20.496029
22	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 14:39:14.782213
23	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 14:50:20.58132
24	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:05:11.390485
25	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-23 15:06:38.477076
26	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:13:45.417596
27	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:22:46.546261
28	/case-study/1	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:23:27.059355
29	/	https://mohamed-maa-albared-portfolio.onrender.com/case-study/1	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:23:55.615301
30	/case-study/2	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:24:01.622969
31	/	https://mohamed-maa-albared-portfolio.onrender.com/case-study/2	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:25:08.234418
32	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:25:14.456564
33	/blog/neural-palette-ai-neuroscience-art-convergence	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:27:09.76032
35	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:32:46.617263
36	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:33:48.793971
38	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:41:09.895585
39	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:47:34.649094
41	/	https://mohamed-maa-albared-portfolio.onrender.com/blog/neural-palette-ai-neuroscience-art-convergence	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:51:29.097357
47	/	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:58:59.084264
51	/		Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-GB	2026-02-23 16:08:56.516036
34	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:31:11.574219
37	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:40:49.141877
40	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:49:22.094224
42	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:51:58.067415
43	/		Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-GB	2026-02-23 15:54:59.091551
44	/		Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-GB	2026-02-23 15:56:34.429763
45	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:57:25.307109
46	/blog	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 15:58:19.755195
48	/		Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-GB	2026-02-23 16:04:58.476931
49	/blog	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 16:08:32.644844
50	/	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 16:08:42.269308
52	/blog	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 18:52:35.613487
53	/blog/neural-palette-ai-neuroscience-art-convergence	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 18:52:48.181672
54	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 18:53:13.649144
55	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 20:18:02.811631
56	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-23 20:25:05.594063
57	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 09:01:39.119606
58	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/experience/1/edit	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 09:04:55.643151
59	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 09:05:33.175244
60	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 09:05:51.531378
61	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 09:05:55.297678
62	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/admin/experience/1/edit	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 09:06:05.051461
63	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 09:06:27.306615
64	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 09:31:46.435613
65	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 09:58:10.535951
66	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/admin/experience/1/edit	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 09:58:53.348935
67	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 10:02:44.114954
68	/case-study/1	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 10:03:35.971378
69	/blog	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 10:05:21.196603
70	/blog/neural-palette-ai-neuroscience-art-convergence	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 10:05:32.171598
71	/blog		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 10:07:31.068552
72	/	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 10:07:50.798646
73	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 10:12:50.175488
74	/	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 10:13:06.126251
75	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 12:41:19.174813
76	/case-study/1	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:06:26.036854
77	/	https://mohamed-maa-albared-portfolio.onrender.com/case-study/2	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:07:34.964338
78	/case-study/3	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:07:38.828628
79	/case-study/2	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:08:49.702727
80	/	https://mohamed-maa-albared-portfolio.onrender.com/case-study/2	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:09:54.245126
81	/blog	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:10:20.672896
82	/blog/neural-canvas-art-neuroscience-ai	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:10:28.171295
83	/blog	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:10:56.288417
84	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:11:01.562334
85	/	https://mohamed-maa-albared-portfolio.onrender.com/blog/architecture-of-thought-neuroscience-ai-agents	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:11:20.848411
86	/		Mozilla/5.0 (compatible; Google-Site-Verification/1.0)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:14:36.733451
87	/		Mozilla/5.0 (compatible; Google-Site-Verification/1.0)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:14:36.837101
88	/googlea137af14418c7a75.html		Mozilla/5.0 (compatible; Google-Site-Verification/1.0)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:14:36.836918
89	/		Mozilla/5.0 (compatible; Google-Site-Verification/1.0)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:14:36.844053
90	/googlebacb5ca0cf90bf4a.html		Mozilla/5.0 (compatible; Google-Site-Verification/1.0)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:14:36.88142
91	/		Mozilla/5.0 (compatible; Google-Site-Verification/1.0)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:14:36.932941
92	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:18:32.62419
93	/		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:19:02.913263
94	/favicon.ico		Googlebot-Image/1.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:19:11.814204
95	/		Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:19:25.605851
96	/		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:19:25.614149
97	/favicon.ico		Googlebot-Image/1.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 13:19:27.972506
98	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/sitemap.xml	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:21:20.53846
99	/	https://mohamed-maa-albared-portfolio.onrender.com/blog/architecture-of-thought-neuroscience-ai-agents	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-24 13:21:25.441633
100	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 16:42:24.788012
101	/blog/neural-palette-ai-neuroscience-art-convergence		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 16:42:26.909444
102	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-24 20:17:39.670905
103	/	http://mohamed-maa-albared-portfolio.onrender.com	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-25 16:26:00.469379
104	/		okhttp/5.3.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-25 20:54:17.445102
105	/favicon.png		okhttp/5.3.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-25 20:54:18.017199
106	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/138.0.7204.23 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-25 20:55:13.31837
107	/	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-25 21:04:06.176209
108	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-25 21:06:02.622102
109	/blog	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-25 21:10:04.678924
110	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-25 21:10:11.957913
111	/	https://mohamed-maa-albared-portfolio.onrender.com/blog/architecture-of-thought-neuroscience-ai-agents	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-25 21:11:12.148129
112	/		Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/144.0.7559.95 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-25 21:16:42.719672
113	/.env		Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-25 23:44:19.163623
114	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-27 04:04:59.712168
115	/	https://mohamed-maa-albared-portfolio.onrender.com/sitemap.xml	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 08:31:54.955205
116	/		Mozilla/5.0 (Linux; Android 11; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36 Chrome-Lighthouse	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 08:35:28.853153
117	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Chrome-Lighthouse	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 08:35:29.1787
118	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Chrome-Lighthouse	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-27 08:35:33.023024
119	/		Mozilla/5.0 (Linux; Android 11; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36 Chrome-Lighthouse	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-27 08:35:33.524425
120	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Chrome-Lighthouse	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-27 08:35:37.743494
121	/		Mozilla/5.0 (Linux; Android 11; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36 Chrome-Lighthouse	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-27 08:35:41.525682
122	/.well-known/traffic-advice		Chrome Privacy Preserving Prefetch Proxy	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-27 08:37:27.586648
123	/	https://www.google.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 08:37:27.6169
124	/	https://www.google.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 08:38:42.764442
125	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 10:02:35.38687
126	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 10:03:39.563346
127	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 10:06:27.05256
128	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 12:40:12.642221
129	/	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 12:41:33.538359
130	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 12:41:54.371783
131	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 14:33:20.599659
132	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 14:37:04.780233
133	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 21:02:28.335675
134	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 21:08:00.913995
135	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 21:08:15.353548
136	/.well-known/traffic-advice		Chrome Privacy Preserving Prefetch Proxy	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-27 21:08:25.042295
137	/	https://www.google.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 21:08:25.062184
138	/		Google-Lens	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-27 21:08:56.223397
139	/		Google-Lens	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-27 21:11:11.530533
140	/		Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/144.0.7559.95 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-27 21:17:37.879597
141	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-28 03:46:51.595724
142	/blog	https://mohamed-maa-albared-portfolio.onrender.com/blog	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-28 14:01:37.736853
143	/blog	https://mohamed-maa-albared-portfolio.onrender.com/blog?category=AI	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-28 14:01:40.423544
144	/	https://mohamed-maa-albared-portfolio.onrender.com/blog?category=Neuroscience	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-02-28 14:01:44.525158
145	/		Mozilla/5.0 (compatible; Google-InspectionTool/1.0;)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-28 17:43:56.152331
146	/		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; Google-InspectionTool/1.0;)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-28 17:43:56.216381
147	/		Mozilla/5.0 (compatible; Google-InspectionTool/1.0;)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-28 17:44:24.184991
148	/		Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-28 17:47:24.564075
149	/		Mozilla/5.0 (compatible; Google-InspectionTool/1.0;)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-02-28 20:15:40.248615
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects (id, title, description, short_description, image_url, demo_url, github_url, technologies, category, year, client, created_at, updated_at, featured, case_study, metrics, challenge, approach, results, has_case_study, sort_order) FROM stdin;
1	Multi-Agent Voice System	Designed and built a live, multi-agent system demo presented as a keynote at the Lufthansa Group Data Community Day 2025. The system processes voice commands, transcribes them, and uses an LLM orchestrator to delegate tasks to specialised search and data analysis agents — solving complex business queries in real-time.	Voice-activated autonomous business analysis.	\N	\N	\N	Python,LLM Orchestration,Whisper,Azure OpenAI,Multi-Agent Systems	genai	2025	Lufthansa Group	2026-02-23 11:56:27.776374	2026-02-23 11:56:27.776377	t	\N	[{"value": "2nd", "label": "Consecutive Year Keynoting"}, {"value": "Live", "label": "Working Demo on Stage"}, {"value": "Voice", "label": "Enabled Multi-Agent System"}, {"value": "3", "label": "Specialised Agents"}]	<p>The Lufthansa Group Data Community Day is the biggest and most sought-after annual data event in the Group. I was tasked with representing zeroG by delivering an advanced presentation on Agentic AI and Multi-Agent Systems. The challenge: go beyond slides and build a <strong>working, voice-activated multi-agent system</strong> that could accept natural voice commands, reason about the intent, and coordinate multiple specialised agents to produce actionable business insights — all live on stage with zero tolerance for failure.</p><p>Traditional chatbots fall short here — they can't decompose complex queries, delegate subtasks, or synthesise information from multiple sources autonomously.</p>	<p>The architecture follows a <strong>hierarchical orchestration pattern</strong>:</p><ul><li><strong>Voice Layer:</strong> Real-time voice transcription converts spoken commands into text</li><li><strong>Orchestrator Agent:</strong> An LLM-powered coordinator that parses intent, decomposes the query into subtasks, and selects the appropriate specialist agent</li><li><strong>Search Agent:</strong> Retrieves relevant information from knowledge bases for research tasks</li><li><strong>Data Analysis Agent:</strong> Handles data queries, computes KPIs, and generates insights for business analysis</li></ul><p>The presentation, titled "LLMs: From Chatty Cathy to Autonomous Agents," walked the audience through the evolution of AI from simple chatbots to autonomous reasoning systems, culminating in the live demo.</p>	<p>The live demo at Data Community Day 2025 was delivered successfully:</p><ul><li>Successfully demonstrated <strong>autonomous task delegation</strong> across specialised agents solving a business query in real-time</li><li>The presentation <strong>sparked significant discussions</strong> about agentic AI adoption across the organisation</li><li>Demonstrated zeroG's <strong>cutting-edge expertise</strong> in autonomous AI systems</li><li>This was my <strong>second consecutive year</strong> keynoting at Data Community Day, reinforcing thought leadership</li></ul>	t	1
4	AB Testing Framework	Led research and development of a comprehensive, generalised AB testing framework. Includes covariate balance checking, ATE analysis, and a sophisticated CATE framework with five meta-learners, SHAP-based customer archetype discovery, and automated dual-reporting (technical and stakeholder). This pipeline became the foundation for a newly created independent Performance Measurement team at the client.	Comprehensive experimentation pipeline with causal inference.	\N	\N	\N	Python,Causal Inference,SHAP,Meta-Learners,Statistical Testing	recsys	2024	Lufthansa Group	2026-02-23 11:56:27.77903	2026-02-23 11:56:27.779033	f	\N	\N	\N	\N	\N	f	4
5	Human Behavior Simulation	Master's thesis combining three AI modalities: Zero-Shot voice cloning, 3D avatar reconstruction (PIFu), and deep RL agent training (PPO).	Multi-modal AI: voice cloning + 3D avatar + RL agent.	\N	\N	\N	Python,TensorFlow,Blender,Unity,C#,PPO	rl cv	2021	Arab International University	2026-02-23 11:56:27.779034	2026-02-23 11:56:27.779034	f	\N	\N	\N	\N	\N	f	5
6	Virtual Patient Simulation	Developed an AI-powered 'Virtual Patient' simulation for interactive clinical training.	Interactive AI patient for medical training scenarios.	\N	\N	\N	Python,NLP,SGD,Classification,Flask	nlp	2022	Freelance Client	2026-02-23 11:56:27.779035	2026-02-23 11:56:27.779036	f	\N	\N	\N	\N	\N	f	6
7	Dark Web Auto-Labelling	Built an automated system for scraping, labelling, and classifying dark web content using NLP-based text classification pipelines.	Automated classification of dark web content.	\N	\N	\N	Python,Scikit-Learn,BeautifulSoup,Selenium,NLP	nlp	2022	Freelance Client	2026-02-23 11:56:27.779036	2026-02-23 11:56:27.779037	f	\N	\N	\N	\N	\N	f	7
8	Emotion Prediction from Voice	Deep learning model predicting human emotions (calm, happy, sad, angry, fearful, surprised, disgusted) from audio files using Inception networks on mel-spectrograms.	Deep learning classifier for vocal emotion detection.	\N	\N	\N	Python,TensorFlow,Keras,Inception,Mel-Spectrogram	cv	2021	Damascus Start-Up	2026-02-23 11:56:27.779037	2026-02-23 11:56:27.779038	f	\N	\N	\N	\N	\N	f	8
9	Arabic Tweets Classifier	Kaggle competition for classifying Arabic tweets into positive, negative, and neutral sentiment classes. Achieved 75.9% accuracy using BERT with extensive Arabic language processing.	Sentiment analysis for Arabic social media text.	\N	\N	\N	Python,BERT,Arabic NLP,Kaggle	nlp	2021	Damascus Start-Up	2026-02-23 11:56:27.779038	2026-02-23 11:56:27.779039	f	\N	\N	\N	\N	\N	f	9
10	Forex Forecasting (JPY/CAD)	Predicting JPY/CAD exchange rates using 20 years of scraped economic data from multiple websites and Reuters news. Combined macroeconomic features from Japan, Canada, and the USA with deep neural networks for prediction.	Time-series model for foreign exchange prediction.	\N	\N	\N	Python,TensorFlow,Web Scraping,Reuters NLP,Deep NN	nlp	2020	Damascus Start-Up	2026-02-23 11:56:27.77904	2026-02-23 11:56:27.77904	f	\N	\N	\N	\N	\N	f	10
11	RAG Pipeline with Smart Segmentation	RAG pipeline with smart document segmentation inspired by Anthropic's research, dynamically chunking documents based on semantic boundaries.	Retrieval-Augmented Generation with semantic chunking.	\N	\N	\N	Python,LangChain,FAISS,Azure OpenAI	genai	2024	Personal Project	2026-02-23 11:56:27.779041	2026-02-23 11:56:27.779041	f	\N	\N	\N	\N	\N	f	11
12	AI Search & Reasoning Agents	Multi-step reasoning AI agents with source credibility assessment, chain-of-thought reasoning, and autonomous tool use.	Multi-step reasoning agents inspired by OpenAI O-series.	\N	\N	\N	Python,LangChain,OpenAI,Tool Use,Agents	genai	2024	Personal Project	2026-02-23 11:56:27.779042	2026-02-23 11:56:27.779042	f	\N	\N	\N	\N	\N	f	12
\.


--
-- Data for Name: site_config; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.site_config (id, key, value, label, "group") FROM stdin;
1	hero_label	DATA SCIENTIST &bull; AI ENGINEER	Label / Title Bar	hero
2	hero_name_line1	MOHAMED	Name Line 1	hero
3	hero_name_line2	MAA ALBARED	Name Line 2	hero
4	hero_tagline_word1	Architecting	Tagline Word 1	hero
5	hero_tagline_word2	Intelligence	Tagline Word 2	hero
6	hero_subtitle	Where neural networks meet creative intuition — building systems that reason, collaborate, and act.	Subtitle	hero
7	about_bio1	Accomplished Data Scientist with over <strong>4 years of experience</strong> specializing in the development and deployment of machine learning and generative AI solutions within the <strong>aviation sector</strong>.	Bio Paragraph 1	about
8	about_bio2	Proven track record of driving significant business value by architecting <strong>recommendation systems</strong>, optimizing model performance by up to <strong>20x</strong>, and pioneering <strong>AB testing frameworks</strong> from the ground up.	Bio Paragraph 2	about
9	about_bio3	Recognized as a subject matter expert in <strong>LLM orchestration</strong> and <strong>autonomous agent design</strong>, adept at translating complex AI capabilities into strategic, impactful business outcomes.	Bio Paragraph 3	about
10	about_years	4	Years of Experience	about
12	about_perf_gains	20	Performance Gains (x)	about
11	about_projects_count	50+	Projects Delivered	about
\.


--
-- Data for Name: skill_clusters; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.skill_clusters (id, icon, title, tags, sort_order) FROM stdin;
1	&#129302;	Generative & Agentic AI	LLM Orchestration, Multi-Agent Systems, Prompt Engineering, RAG Pipelines, Fine-Tuning, LangChain/LangGraph, Semantic Kernel	1
2	&#129504;	ML & Data Science	Recommendation Systems, NLP/NLU, Classification, Regression, Feature Engineering, A/B Testing, XGBoost, Deep Learning	2
3	&#128187;	Tech Stack	Python, SQL, Flask, FastAPI, TensorFlow, PyTorch, scikit-learn, Pandas, NumPy, Git, REST APIs	3
4	&#9729;	Cloud & MLOps	Azure ML, AWS (S3, Lambda), Docker, CI/CD, MLflow, Weights & Biases, Databricks, Airflow	4
\.


--
-- Name: blog_posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.blog_posts_id_seq', 5, true);


--
-- Name: experiences_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.experiences_id_seq', 5, true);


--
-- Name: impact_cards_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.impact_cards_id_seq', 4, true);


--
-- Name: language_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.language_items_id_seq', 3, true);


--
-- Name: messages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.messages_id_seq', 1, true);


--
-- Name: page_visits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.page_visits_id_seq', 149, true);


--
-- Name: projects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_id_seq', 12, true);


--
-- Name: site_config_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.site_config_id_seq', 12, true);


--
-- Name: skill_clusters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.skill_clusters_id_seq', 4, true);


--
-- Name: blog_posts blog_posts_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_posts
    ADD CONSTRAINT blog_posts_pkey PRIMARY KEY (id);


--
-- Name: blog_posts blog_posts_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.blog_posts
    ADD CONSTRAINT blog_posts_slug_key UNIQUE (slug);


--
-- Name: experiences experiences_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.experiences
    ADD CONSTRAINT experiences_pkey PRIMARY KEY (id);


--
-- Name: impact_cards impact_cards_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.impact_cards
    ADD CONSTRAINT impact_cards_pkey PRIMARY KEY (id);


--
-- Name: language_items language_items_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.language_items
    ADD CONSTRAINT language_items_pkey PRIMARY KEY (id);


--
-- Name: messages messages_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id);


--
-- Name: page_visits page_visits_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.page_visits
    ADD CONSTRAINT page_visits_pkey PRIMARY KEY (id);


--
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);


--
-- Name: projects projects_title_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_title_key UNIQUE (title);


--
-- Name: site_config site_config_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.site_config
    ADD CONSTRAINT site_config_pkey PRIMARY KEY (id);


--
-- Name: skill_clusters skill_clusters_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.skill_clusters
    ADD CONSTRAINT skill_clusters_pkey PRIMARY KEY (id);


--
-- Name: ix_page_visits_visited_at; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_page_visits_visited_at ON public.page_visits USING btree (visited_at);


--
-- Name: ix_site_config_key; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_site_config_key ON public.site_config USING btree (key);


--
-- PostgreSQL database dump complete
--

\unrestrict g78XSuhZZ2Cduo3Yk876t8nm6Hh4jA7IEUdgF2AfsEinT0OmxWp7qbdYJ31PMmp

