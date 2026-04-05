--
-- PostgreSQL database dump
--

\restrict 7fsMfOTm97TK2oF9tpDm6A3svNCAfetGc1Ik5UoX3kWoHopracLuKWpHXICgw7t

-- Dumped from database version 17.8 (a48d9ca)
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


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS '';


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
    sort_order integer,
    title_ar text,
    excerpt_ar text,
    content_ar text
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
    sort_order integer,
    role_ar text,
    description_ar text,
    highlights_ar text
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
    sort_order integer,
    description_ar text
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
    sort_order integer,
    title_ar text,
    short_description_ar text,
    description_ar text,
    challenge_ar text,
    approach_ar text,
    results_ar text,
    case_study_ar text
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
    sort_order integer,
    title_ar text,
    tags_ar text
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

COPY public.blog_posts (id, title, slug, excerpt, content, cover_image, category, tags, read_time, published, featured, created_at, updated_at, sort_order, title_ar, excerpt_ar, content_ar) FROM stdin;
1	The Architecture of Thought: How Neuroscience Is Inspiring the Next Wave of AI Agents	architecture-of-thought-neuroscience-ai-agents	Your prefrontal cortex is the world's most sophisticated AI orchestrator — delegating tasks, managing working memory, and coordinating specialised brain regions. Recent neuroscience reveals striking parallels with modern multi-agent AI architectures.	<h2>The Brain's Original Multi-Agent Architecture</h2>\n<p>When I built a <strong>multi-agent voice system</strong> for Lufthansa Group's Data Community Day — a system where an LLM orchestrator delegates tasks to specialised search and data analysis agents — I wasn't just engineering software. I was, unknowingly, replicating one of the brain's oldest design patterns.</p>\n<p>The prefrontal cortex (PFC) doesn't do everything itself. It's an <em>executive coordinator</em> — remarkably similar to the orchestrator agent pattern now dominating AI system design. And recent neuroscience research reveals just how deep this parallel runs.</p>\n<h2>The Prefrontal Cortex as Orchestrator</h2>\n<p>A landmark 2024 study published in <em>Nature Neuroscience</em> by Rigotti et al. demonstrated that prefrontal neurons exhibit <strong>"mixed selectivity"</strong> — they respond to complex combinations of task variables rather than single features. This is strikingly similar to how LLM-based orchestrators process multi-dimensional context before deciding which specialist to invoke.</p>\n<p>Here's what most people don't realize: <strong>your brain runs on roughly 20 watts of power</strong> — less than a laptop charger. Yet it coordinates approximately 86 billion neurons across hundreds of specialised regions, maintaining coherent behaviour through what neuroscientists call <em>hierarchical predictive processing</em>.</p>\n<blockquote>\n<p>"The brain doesn't process information — it <em>predicts</em> it. Every neural circuit is running a generative model of the world, constantly updating its predictions against incoming sensory data."</p>\n<p>— Karl Friston, Free Energy Principle</p>\n</blockquote>\n<h2>Surprising Parallel: Attention in Brains and Transformers</h2>\n<p>The transformer architecture's <strong>attention mechanism</strong> — the foundation of every modern LLM — bears a remarkable resemblance to the brain's selective attention system. In 2023, researchers at DeepMind and UCL showed that the mathematical operations underlying multi-head attention are functionally equivalent to what hippocampal place cells do when navigating spatial environments.</p>\n<p>But here's what's truly unexpected: the brain invented something even more sophisticated. <strong>Predictive coding theory</strong> suggests that the cortex operates as a hierarchy of generative models, where each level predicts the activity of the level below and only forwards <em>prediction errors</em>. This is more efficient than attention — it only transmits what's surprising.</p>\n<p>This insight is now influencing next-generation AI architectures. Papers from Anthropic and Google DeepMind in 2025 are exploring "predictive routing" mechanisms that could make transformer inference dramatically more efficient by only processing tokens that violate the model's expectations.</p>\n<h2>The Workspace Theory: What Consciousness Teaches AI</h2>\n<p>Cognitive scientist Bernard Baars proposed the <strong>Global Workspace Theory (GWT)</strong> of consciousness in the 1980s — the idea that consciousness emerges from a "workspace" where specialised cognitive modules compete for access to broadcast their information globally.</p>\n<p>Sound familiar? It's precisely the architecture of modern multi-agent AI systems:</p>\n<ul>\n<li><strong>Specialised agents</strong> = specialised brain modules (Broca's area for language, fusiform face area for facial recognition, etc.)</li>\n<li><strong>Orchestrator/dispatcher</strong> = the global workspace (prefrontal cortex + thalamus)</li>\n<li><strong>Context window</strong> = working memory (limited to ~4 chunks, just like the 7 plus/minus 2 items in human short-term memory)</li>\n</ul>\n<p>In my work building agentic systems at zeroG, I've found that the most robust agent architectures mirror this neural blueprint: a coordinator that maintains state, specialist agents that process domain-specific queries, and a shared context that accumulates findings — just like the brain's working memory.</p>\n<h2>The Cerebellum: Nature's Pre-Trained Model</h2>\n<p>Here's a fact that shocks most AI researchers: <strong>the cerebellum contains more neurons than the rest of the brain combined</strong> (~69 billion out of ~86 billion). Yet neuroscience has largely ignored it, calling it the "little brain" responsible for mere motor coordination.</p>\n<p>Recent research paints a radically different picture. The cerebellum appears to function as a <strong>universal prediction engine</strong> — it builds forward models of everything: motor sequences, language patterns, social expectations, even abstract thought. When you finish someone's sentence, your cerebellum predicted it 300ms before they said it.</p>\n<p>This is essentially what pre-training does for LLMs. The cerebellum is nature's answer to "How do you build a foundation model?" — a massive, uniform neural network trained on the statistics of life experience to predict what comes next.</p>\n<h2>From Brains to Systems: Engineering Lessons</h2>\n<p>After years of building AI systems professionally and studying neuroscience as a personal passion, I've identified three principles that emerge from both disciplines:</p>\n<ol>\n<li><strong>Delegation over computation:</strong> The brain doesn't compute everything centrally. Neither should your AI system. Specialise and delegate.</li>\n<li><strong>Prediction over reaction:</strong> The most efficient systems anticipate rather than respond. Build predictive models, not just reactive pipelines.</li>\n<li><strong>Error signals over raw data:</strong> The brain transmits surprises, not observations. Design systems that focus on what's unexpected — it's where the information lives.</li>\n</ol>\n<p>The next frontier in AI isn't just more parameters or bigger context windows. It's learning from the architecture that 600 million years of evolution already optimised — the architecture of thought itself.</p>\n<p><em>This article reflects insights from my research and hands-on experience building multi-agent AI systems at zeroG (Lufthansa Group). The neuroscience references draw from peer-reviewed research published in Nature Neuroscience, Neuron, and Trends in Cognitive Sciences.</em></p>	\N	Neuroscience	Neuroscience,Agentic AI,Multi-Agent Systems,Prefrontal Cortex,LLM Orchestration	12	t	t	2026-02-15 00:00:00	2026-03-02 11:43:26.384365	1	بنيان الفكر: كيف يُلهم علم الأعصاب الجيل القادم من وكلاء الذكاء الاصطناعي	قشرتك الجبهية الأمامية هي أكثر منسّقات الذكاء الاصطناعي احترافاً في العالم — تفوّض المهام، وتدير الذاكرة العاملة، وتنسّق مناطق دماغية متخصصة. يكشف علم الأعصاب الحديث عن تشابهات مذهلة مع بنيات الذكاء الاصطناعي متعددة الوكلاء.	<h2>البنية الأصلية للدماغ متعددة الوكلاء</h2>\n<p>حين بنيت <strong>نظام صوتي متعدد الوكلاء</strong> ليوم مجتمع بيانات مجموعة لوفتهانزا — نظام يفوّض فيه منسّق LLM المهام إلى وكلاء بحث وتحليل بيانات متخصصة — لم أكن أطوّر برمجيات فحسب. كنت، دون أن أدري، أُعيد إنتاج أحد أقدم أنماط تصميم الدماغ.</p>\n<p>القشرة الجبهية الأمامية (PFC) لا تفعل كل شيء بنفسها. إنها <em>منسّق تنفيذي</em> — تشبه بشكل لافت نمط وكيل المنسّق الذي يهيمن الآن على تصميم أنظمة الذكاء الاصطناعي.</p>\n<h2>القشرة الجبهية الأمامية كمنسّق</h2>\n<p>كشفت دراسة بارزة نُشرت عام 2024 في <em>Nature Neuroscience</em> أن الخلايا العصبية الجبهية تُظهر <strong>"الانتقائية المختلطة"</strong> — حيث تستجيب لمجموعات معقدة من متغيرات المهمة لا لسمة واحدة. هذا مشابه بشكل لافت لكيفية معالجة المنسّقات القائمة على LLM للسياق متعدد الأبعاد قبل تحديد الوكيل المناسب.</p>\n<h2>نظرية الفضاء العالمي: ما يعلّمنا الوعي عن الذكاء الاصطناعي</h2>\n<p>اقترح عالم الإدراك برنارد بارس <strong>نظرية مساحة العمل العالمية (GWT)</strong> للوعي في الثمانينيات — فكرة أن الوعي ينشأ من "مساحة عمل" تتنافس فيها الوحدات المعرفية المتخصصة للوصول وبث معلوماتها عالمياً.</p>\n<h2>دروس هندسية</h2>\n<ol>\n<li><strong>التفويض على الحساب:</strong> الدماغ لا يحسب كل شيء مركزياً. كذلك لا ينبغي لنظام الذكاء الاصطناعي. تخصّص وفوّض.</li>\n<li><strong>التنبؤ على ردّ الفعل:</strong> الأنظمة الأكثر كفاءة تتوقع بدلاً من أن تستجيب.</li>\n<li><strong>إشارات الخطأ على البيانات الخام:</strong> الدماغ ينقل المفاجآت لا الملاحظات. صمّم أنظمة تركّز على ما هو غير متوقع.</li>\n</ol>
2	From Chatty Cathy to Autonomous Reasoners: The Agentic AI Revolution	agentic-ai-revolution-autonomous-reasoners	We're witnessing the most fundamental shift in AI since deep learning: the transition from models that chat to systems that reason, plan, and act. Here's what's really happening behind the hype — and what I've learned building these systems.	<h2>The Quiet Revolution</h2>\n<p>In 2023, you asked an LLM a question and it answered. In 2024, you asked it to accomplish a goal and it wrote code. In 2025, you described a <em>problem</em> and it assembled a team of agents to solve it autonomously.</p>\n<p>This isn't incremental progress. It's a phase transition. And having built one of these systems live on stage — <strong>a voice-activated multi-agent system for the Lufthansa Group Data Community Day</strong> — I can tell you the gap between "chatbot" and "autonomous agent" is larger than most people appreciate.</p>\n<h2>What Actually Changed?</h2>\n<p>Three breakthroughs converged to make agentic AI possible:</p>\n<h3>1. Reliable Tool Use</h3>\n<p>The moment LLMs could <strong>reliably call functions</strong> — querying databases, invoking APIs, running code — they stopped being conversationalists and became operators. OpenAI's function calling, Anthropic's tool use, and Google's extensions all shipped within months of each other in 2023-2024.</p>\n<h3>2. Chain-of-Thought Reasoning</h3>\n<p>The publication of <strong>ReAct (Reasoning + Acting)</strong> by Yao et al. showed that interleaving reasoning traces with action steps dramatically improved task completion rates. But here's the underappreciated insight: ReAct works because it externalises the model's "thinking" — making its planning process legible and debuggable.</p>\n<p>In my own work, I've found that the quality of an agent system depends less on the model's raw intelligence and more on <strong>the quality of its reasoning scaffolding</strong>. Give a mediocre model great tools and clear reasoning templates, and it will outperform a frontier model with poor scaffolding.</p>\n<h3>3. Multi-Agent Coordination</h3>\n<p>Single agents hit a ceiling quickly. The breakthrough came from <strong>splitting responsibilities</strong> across specialised agents — mirroring how human organisations work.</p>\n<h2>What Most People Get Wrong</h2>\n<p>Having built and deployed agentic systems at enterprise scale, here's what the hype cycle misses:</p>\n<h3>The Reliability Problem Is Not Solved</h3>\n<p>"Demo-quality" agent systems fail spectacularly in production. A system that works 90% of the time in a demo fails roughly <strong>every 10th customer interaction</strong>. When I designed the live demo for Data Community Day, I spent 70% of development time on error handling, fallback strategies, and graceful degradation — not on the "cool" agent orchestration.</p>\n<h3>Latency Is the Silent Killer</h3>\n<p>Multi-step agent reasoning introduces <strong>compounding latency</strong>. Each LLM call adds 1-3 seconds. A four-step reasoning chain takes 8-12 seconds. The solution isn't faster models — it's better <strong>architecture</strong>: parallel agent execution, speculative tool calling, and aggressive caching.</p>\n<h3>The 95% Problem</h3>\n<p>Here's the number that haunts every agent builder: <strong>95% of your users won't have the data you need to personalise for them</strong>. At Lufthansa Group, 95%+ of website visitors are non-logged-in. Our solution — using generative AI to synthesise "category profiles" for destinations — was born from this constraint.</p>\n<h2>Where This Is Going</h2>\n<p>The next two years will see three major developments:</p>\n<ol>\n<li><strong>Agent Operating Systems:</strong> Standardised "operating systems" for agents — with process management, memory systems, and inter-agent communication protocols. Model Context Protocol (MCP) is an early example.</li>\n<li><strong>Specialised Agent Hardware:</strong> New silicon optimised for the frequent, small, context-heavy calls that agent systems make.</li>\n<li><strong>Agent-Native Applications:</strong> Applications where the entire UX is built around an autonomous agent that happens to have a human-friendly interface.</li>\n</ol>\n<p>We're not building smarter chatbots. We're building a new kind of software — software that reasons, plans, and acts. <strong>The agent era is the main event.</strong></p>\n<p><em>Based on hands-on experience building production agentic AI systems at zeroG (Lufthansa Group).</em></p>	\N	AI	Agentic AI,LLM,Autonomous Agents,ReAct,Tool Use,Reasoning	10	t	t	2026-02-01 00:00:00	2026-03-02 11:43:26.386006	2	من روبوتات الدردشة إلى العقلاء المستقلين: ثورة الذكاء الاصطناعي العملي	نشهد أعمق تحوّل في الذكاء الاصطناعي منذ التعلم العميق: الانتقال من نماذج تتحدث إلى أنظمة تستدل وتخطط وتتصرف. إليك ما يحدث فعلاً وراء الضجيج — وما تعلمته من بناء هذه الأنظمة.	<h2>الثورة الهادئة</h2>\n<p>في 2023، كنت تسأل نموذج لغوياً فيجيب. في 2024، طلبت منه إنجاز هدف فكتب كوداً. في 2025، وصفت <em>مشكلة</em> فجمّع فريقاً من الوكلاء لحلها باستقلالية.</p>\n<p>هذا ليس تقدماً تدريجياً. إنه تحوّل جذري. وبعد أن بنيت أحد هذه الأنظمة على المسرح مباشرة — <strong>نظام صوتي متعدد الوكلاء ليوم مجتمع بيانات مجموعة لوفتهانزا</strong> — أستطيع القول إن الهوة بين "روبوت الدردشة" و"الوكيل المستقل" أضخم مما يُقدِّر معظم الناس.</p>\n<h2>ما الذي تغيّر فعلاً؟</h2>\n<h3>1. استخدام الأدوات بموثوقية</h3>\n<p>في اللحظة التي أصبحت فيها نماذج اللغة الكبيرة قادرة على <strong>استدعاء الدوال بموثوقية</strong> — استعلام قواعد البيانات، واستدعاء الواجهات البرمجية، وتشغيل الكود — توقفت عن كونها محادِثة وأصبحت مشغِّلة.</p>\n<h3>2. الاستدلال بسلسلة الأفكار</h3>\n<p>أظهر نشر <strong>ReAct (الاستدلال + التصرف)</strong> بواسطة Yao et al. أن التناوب بين آثار الاستدلال وخطوات التصرف حسّن بشكل كبير معدلات إتمام المهام.</p>\n<h3>3. تنسيق الوكلاء المتعددين</h3>\n<p>الوكلاء الفرديون يصطدمون بسقف سريعاً. جاء الاختراق من <strong>تقسيم المسؤوليات</strong> عبر وكلاء متخصصين — مرايا لكيفية عمل المنظمات البشرية.</p>\n<h2>إلى أين يسير هذا؟</h2>\n<ol>\n<li><strong>أنظمة تشغيل الوكلاء:</strong> منصات معيارية مع إدارة العمليات وأنظمة الذاكرة وبروتوكولات التواصل بين الوكلاء. MCP مثال مبكر.</li>\n<li><strong>أجهزة الوكلاء المتخصصة:</strong> شرائح جديدة محسّنة للاستدعاءات الصغيرة والمتكررة والمحمّلة بالسياق.</li>\n<li><strong>تطبيقات أصيلة للوكلاء:</strong> تطبيقات يُبنى فيها تجربة المستخدم بالكامل حول وكيل مستقل.</li>\n</ol>
3	The Neural Canvas: Where Art, Neuroscience, and AI Converge	neural-canvas-art-neuroscience-ai	Your brain's visual cortex uses operations remarkably similar to convolutional neural networks. Beauty activates the same reward circuits as food and sex. And AI is now creating art that triggers genuine aesthetic experiences. The convergence of these fields is revealing something profound.	<h2>When Your Brain Looks at Art, It's Running a Neural Network</h2>\n<p>In 2014, neuroscientist Semir Zeki published a finding that would bridge two worlds: when humans experience beauty — whether in visual art, music, or mathematical equations — it activates a specific region of the medial orbito-frontal cortex. The same region. Every time.</p>\n<p>This wasn't just a curious observation. It suggested something radical: <strong>beauty is a computation</strong>, not just a feeling. And if beauty is a computation, then it can — at least in principle — be understood, modelled, and perhaps even generated by artificial systems.</p>\n<h2>The Hidden Mathematics of Visual Perception</h2>\n<p>Here's something that most people don't realize: <strong>the primate visual cortex was the direct inspiration for convolutional neural networks (CNNs)</strong>.</p>\n<p>In 1962, Hubel and Wiesel discovered that neurons in the visual cortex are organised hierarchically:</p>\n<ul>\n<li><strong>V1 (primary visual cortex):</strong> Detects edges and orientations — exactly like the first layers of a CNN</li>\n<li><strong>V2:</strong> Combines edges into textures and simple shapes — like middle CNN layers</li>\n<li><strong>V4:</strong> Processes colour and complex forms — analogous to deeper feature maps</li>\n<li><strong>IT (inferotemporal cortex):</strong> Recognises objects and faces — like the final classification layers</li>\n</ul>\n<p>This isn't a loose analogy. The mathematical operations are <em>functionally identical</em>: spatial convolutions followed by nonlinear activation functions followed by pooling. Evolution discovered deep learning 500 million years before Yann LeCun.</p>\n<h2>Neuroaesthetics: The Science of Why You Stop at a Painting</h2>\n<h3>The Processing Fluency Effect</h3>\n<p>We find images more beautiful when our brains can process them efficiently. This explains why we're drawn to <strong>symmetry, golden ratios, and fractal patterns</strong>. But there's a twist: <em>too much</em> fluency is boring. Peak aesthetic experience occurs at the boundary between order and surprise — <strong>"optimal complexity."</strong></p>\n<h3>The Surprise Paradox</h3>\n<p>The most memorable art violates our expectations while still being interpretable. Neuroimaging studies show that <strong>surprise activates the dopamine system</strong> — the same circuitry involved in learning and reward. Great art is literally teaching us something — reshaping our internal models.</p>\n<h2>My Thesis: Bridging Art, Body, and Machine</h2>\n<p>My master's thesis, <strong>"Human Behavior Simulation,"</strong> was an attempt to bridge this convergence directly, combining three modalities:</p>\n<ol>\n<li><strong>Voice Cloning (Zero-Shot Learning):</strong> Synthesising a human voice from just 5-20 seconds of audio — the most personal form of human artistic expression, reproduced through neural networks</li>\n<li><strong>3D Avatar Reconstruction (PIFu):</strong> Generating a fully rigged 3D avatar from a single photograph — art transformed into a three-dimensional digital being</li>\n<li><strong>Deep Reinforcement Learning (PPO):</strong> Teaching the avatar to walk through trial and error — creating an unintentionally beautiful choreography of machine learning</li>\n</ol>\n<h2>GANs: The Brain's Own Generative Model</h2>\n<p>Generative Adversarial Networks mirror a fascinating aspect of brain function. The brain actively <strong>generates predictions</strong> about what it expects to see, then compares against actual input. This is essentially the GAN architecture: a generator (cortical prediction) and a discriminator (error detection).</p>\n<p>When you look at art and it takes a moment to "resolve," you're experiencing this generative process in real-time. The aesthetic pleasure comes from the <em>resolution</em> itself: your brain successfully updating its generative model to accommodate something new.</p>\n<h2>The Future: Computational Creativity</h2>\n<p>For the first time, we have AI systems that can <em>generate</em> aesthetic content, neuroscience tools that can <em>measure</em> aesthetic experience, and mathematical frameworks to <em>model</em> the relationship. The convergence isn't about machines replacing artists — it's about <strong>understanding creativity itself</strong>.</p>\n<p>The neural canvas is being painted from both sides: biology and silicon. And the picture emerging is more beautiful than either side could create alone.</p>\n<p><em>This article draws from research in neuroaesthetics, computational neuroscience, and my experience building multi-modal AI systems including voice cloning, 3D reconstruction, and deep reinforcement learning.</em></p>	\N	Art	Neuroaesthetics,Generative Art,Neural Style Transfer,Creativity,GANs,Voice Cloning	14	t	t	2026-01-15 00:00:00	2026-03-02 11:43:26.387408	3	اللوحة العصبية: حيث يتلاقى الفن وعلم الأعصاب والذكاء الاصطناعي	القشرة البصرية في دماغك تستخدم عمليات مشابهة بشكل ملحوظ للشبكات العصبية التلافيفية. الجمال يُنشّط دوائر المكافأة ذاتها كالطعام. والذكاء الاصطناعي يبتكر الآن فناً يُثير تجارب جمالية حقيقية. يكشف تلاقي هذه المجالات عن شيء عميق.	<h2>حين ينظر دماغك إلى الفن، فهو يشغّل شبكة عصبية</h2>\n<p>في عام 2014، نشر عالم الأعصاب سمير زيكي اكتشافاً يجسر عالمين: حين يختبر البشر الجمال — سواء في الفن البصري أو الموسيقى أو المعادلات الرياضية — فإنه يُنشّط منطقة محددة في القشرة الحجاجية الأمامية الوسطى. المنطقة ذاتها. في كل مرة.</p>\n<p>لم يكن هذا مجرد ملاحظة فضولية. إنه يُشير إلى شيء جذري: <strong>الجمال عملية حسابية</strong>، لا مجرد شعور.</p>\n<h2>الرياضيات الخفية للإدراك البصري</h2>\n<p>شيء لا يدركه معظم الناس: <strong>القشرة البصرية للرئيسيات كانت مصدر الإلهام المباشر للشبكات العصبية التلافيفية (CNNs)</strong>.</p>\n<p>في عام 1962، اكتشف هيوبل وويزل أن الخلايا العصبية في القشرة البصرية منظّمة هرمياً:</p>\n<ul>\n<li><strong>V1 (القشرة البصرية الأولية):</strong> تكشف الحواف والاتجاهات — تماماً كالطبقات الأولى في CNN</li>\n<li><strong>V4:</strong> تعالج الألوان والأشكال المعقدة — مشابهة لخرائط الميزات العميقة</li>\n<li><strong>IT (القشرة الصدغية السفلية):</strong> تتعرف على الأجسام والوجوه — كالطبقات التصنيفية النهائية</li>\n</ul>\n<h2>الشبكات التوليدية التنافسية: النموذج التوليدي للدماغ</h2>\n<p>تعكس GANs جانباً رائعاً من وظيفة الدماغ. الدماغ يُولّد بنشاط <strong>تنبؤات</strong> بما يتوقع رؤيته، ثم يقارنها بالمدخلات الفعلية. هذه هي بنية GAN في جوهرها: مولّد (التنبؤ القشري) ومُميِّز (كشف الأخطاء).</p>\n<h2>المستقبل: الإبداع الحسابي</h2>\n<p>للمرة الأولى، لدينا أنظمة ذكاء اصطناعي تستطيع <em>توليد</em> المحتوى الجمالي، وأدوات علم الأعصاب التي تستطيع <em>قياس</em> التجربة الجمالية، وأُطر رياضية لـ<em>نمذجة</em> العلاقة. اللوحة العصبية تُرسم من الجانبين: البيولوجيا والسيليكون.</p>
4	Recommendation Systems at 30,000 Feet: Engineering Serendipity in Aviation	recommendation-systems-aviation-engineering-serendipity	Building recommendation systems for airlines is nothing like Netflix or Spotify. 95% of users are anonymous, purchases are infrequent and high-stakes, and a 'wrong' recommendation can cost real money. Here's what I learned engineering serendipity in aviation.	<h2>This Is Not Netflix</h2>\n<p>When people think "recommendation systems," they think Netflix suggesting movies or Spotify building playlists. These scenarios share a key advantage: <strong>abundant user data</strong>.</p>\n<p>Now imagine building a recommendation system where:</p>\n<ul>\n<li><strong>95% of your users are completely anonymous</strong></li>\n<li>The average user interacts <strong>2-3 times per year</strong></li>\n<li>A single purchase can cost <strong>hundreds or thousands of euros</strong></li>\n<li>You're serving <strong>5+ different airline brands</strong></li>\n</ul>\n<p>Welcome to airline recommendation systems. This has been my world at zeroG (Lufthansa Group) for the past three years.</p>\n<h2>The Cold Start Problem at Scale</h2>\n<p>For most platforms, cold-start users are 10-20% of traffic. For airlines, it's <strong>95%+</strong>.</p>\n<p>What we CAN use: contextual signals (route, travel dates, cabin class, market, device type), aggregate patterns, and our generative AI city model that scores destinations across interest categories.</p>\n<h2>The Art of Measuring Impact</h2>\n<p>Building the recommendation system was hard. <strong>Proving it worked</strong> was harder. I built an AB testing framework from the ground up handling two different segmentation paradigms — logged-in users (by ID) and non-logged-in users (by market-behaviour clusters).</p>\n<p>The key insight: <strong>statistical significance doesn't equal business significance</strong>. We built automated dual-reporting showing both statistical and business impact per segment. This framework eventually led to the <strong>creation of a new team</strong> dedicated to performance measurement.</p>\n<h2>The 20x Optimisation</h2>\n<p>The biggest improvement wasn't a better model — it was a better <strong>API architecture</strong>. Vectorised scoring, connection pooling, response caching, and lazy loading achieved a <strong>20x performance improvement</strong>. Same model, same accuracy, but now fast enough for real-time use.</p>\n<h2>What Airlines Can Teach Silicon Valley</h2>\n<ol>\n<li><strong>Anonymous users aren't empty — they're just different.</strong> Every interaction carries contextual information.</li>\n<li><strong>Measurement infrastructure > model sophistication.</strong> A mediocre model with great AB testing will outperform a brilliant model you can't evaluate.</li>\n<li><strong>Performance IS product quality.</strong> A 5-second recommendation will never be deployed at the point of maximum impact.</li>\n<li><strong>Cross-partner generalisation is hard.</strong> Culturally-aware, market-specific adaptations matter enormously.</li>\n</ol>\n<p><em>Based on 3+ years building recommendation systems at zeroG (Lufthansa Group).</em></p>	\N	AI	Recommendation Systems,Aviation,Cold Start,AB Testing,Personalisation,Machine Learning	11	t	f	2025-12-20 00:00:00	2026-03-02 11:43:26.388835	4	أنظمة التوصية على ارتفاع 30,000 قدم: هندسة المصادفة السعيدة في الطيران	بناء أنظمة التوصية للطيران لا يشبه Netflix أو Spotify في شيء. 95% من المستخدمين مجهولون، والمشتريات نادرة وعالية المخاطر، والتوصية 'الخاطئة' قد تُكلّف أموالاً حقيقية. إليك ما تعلمته من هندسة المصادفة السعيدة في قطاع الطيران.	<h2>هذا ليس Netflix</h2>\n<p>حين يفكر الناس في "أنظمة التوصية"، يفكرون في اقتراحات Netflix للأفلام أو Spotify في قوائم التشغيل. تشترك هذه السيناريوهات في ميزة رئيسية: <strong>بيانات مستخدم وفيرة</strong>.</p>\n<p>الآن تخيّل بناء نظام توصية حيث:</p>\n<ul>\n<li><strong>95% من مستخدميك مجهولون تماماً</strong></li>\n<li>يتفاعل المستخدم العادي <strong>2-3 مرات سنوياً</strong> فقط</li>\n<li>قد تُكلّف عملية الشراء الواحدة <strong>مئات أو آلاف اليوروهات</strong></li>\n</ul>\n<p>مرحباً بك في أنظمة توصية شركات الطيران. كان هذا عالمي في zeroG (مجموعة لوفتهانزا) على مدى السنوات الثلاث الماضية.</p>\n<h2>مشكلة البدء البارد على نطاق واسع</h2>\n<p>لمعظم المنصات، يشكّل مستخدمو البدء البارد 10-20% من الحركة. لشركات الطيران، هم <strong>أكثر من 95%</strong>.</p>\n<h2>فن قياس التأثير</h2>\n<p>بناء نظام التوصية كان صعباً. <strong>إثبات نجاحه</strong> كان أصعب. بنيت إطار اختبار AB من الصفر يتعامل مع نموذجَين مختلفَين للتجزئة.</p>\n<p>الرؤية الرئيسية: <strong>الأهمية الإحصائية لا تساوي الأهمية التجارية</strong>.</p>\n<h2>تحسين الأداء بمقدار 20 ضعفاً</h2>\n<p>أكبر تحسين لم يكن نموذجاً أفضل — بل <strong>بنية واجهة برمجية أفضل</strong>. حققت التقييم المتجهي والتجمع وتخزين الاستجابات مؤقتاً والتحميل الكسول <strong>تحسيناً في الأداء بمقدار 20 ضعفاً</strong>.</p>
\.


--
-- Data for Name: experiences; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.experiences (id, role, company, location, date_range, description, highlights, sort_order, role_ar, description_ar, highlights_ar) FROM stdin;
3	Engineering Lecturer (Part-Time)	Arab International University	Damascus, Syria	Feb 2022 — Jun 2022	Instructed undergraduate students in Algorithms &amp; Data Structures. Developed curriculum, projects, and assessments.	["<span class=\\"accent-hl\\">Algorithms &amp; Data Structures</span> lab instructor", "Delivered <span class=\\"accent-hl\\">Reinforcement Learning workshop</span> (Smart Tech Institute, 2021)"]	3	محاضر هندسة (دوام جزئي)	تدريس طلاب البكالوريوس في الخوارزميات وهياكل البيانات. تطوير المناهج والمشاريع والتقييمات.	["\\u0645\\u062f\\u0631\\u0651\\u0628 \\u0645\\u062e\\u062a\\u0628\\u0631 <strong>\\u0627\\u0644\\u062e\\u0648\\u0627\\u0631\\u0632\\u0645\\u064a\\u0627\\u062a \\u0648\\u0647\\u064a\\u0627\\u0643\\u0644 \\u0627\\u0644\\u0628\\u064a\\u0627\\u0646\\u0627\\u062a</strong>", "\\u062a\\u0642\\u062f\\u064a\\u0645 \\u0648\\u0631\\u0634\\u0629 \\u0639\\u0645\\u0644 <strong>\\u0627\\u0644\\u062a\\u0639\\u0644\\u0645 \\u0627\\u0644\\u0645\\u0639\\u0632\\u0632</strong> (\\u0645\\u0639\\u0647\\u062f \\u0627\\u0644\\u062a\\u0643\\u0646\\u0648\\u0644\\u0648\\u062c\\u064a\\u0627 \\u0627\\u0644\\u0630\\u0643\\u064a\\u0629\\u060c 2021)"]
4	Data Scientist	Damascus-based Start-Up	Damascus, Syria	Apr 2020 — Jun 2021	Owned the full data science pipeline — from web scraping and cleaning to modelling and deployment of predictive systems.	["<span class=\\"accent-hl\\">Foreign Exchange Forecasting</span> (JPY/CAD) \\u2014 time-series model", "<span class=\\"accent-hl\\">Emotion Prediction from Voice</span> \\u2014 deep learning classifier", "<span class=\\"accent-hl\\">Arabic Tweets Classifier</span> \\u2014 NLP sentiment analysis"]	4	عالم بيانات	إدارة منظومة علم البيانات الكاملة، من جمع البيانات وتنظيفها إلى بناء النماذج ونشر الأنظمة التنبؤية.	["<strong>\\u0627\\u0644\\u062a\\u0646\\u0628\\u0624 \\u0628\\u0623\\u0633\\u0639\\u0627\\u0631 \\u0627\\u0644\\u0635\\u0631\\u0641</strong> (JPY/CAD) \\u2013 \\u0646\\u0645\\u0648\\u0630\\u062c \\u0627\\u0644\\u0633\\u0644\\u0627\\u0633\\u0644 \\u0627\\u0644\\u0632\\u0645\\u0646\\u064a\\u0629", "<strong>\\u0627\\u0644\\u062a\\u0646\\u0628\\u0624 \\u0628\\u0627\\u0644\\u0645\\u0634\\u0627\\u0639\\u0631 \\u0645\\u0646 \\u0627\\u0644\\u0635\\u0648\\u062a</strong> \\u2013 \\u0645\\u0635\\u0646\\u0651\\u0641 \\u062a\\u0639\\u0644\\u0645 \\u0639\\u0645\\u064a\\u0642", "<strong>\\u0645\\u0635\\u0646\\u0651\\u0641 \\u0627\\u0644\\u062a\\u063a\\u0631\\u064a\\u062f\\u0627\\u062a \\u0627\\u0644\\u0639\\u0631\\u0628\\u064a\\u0629</strong> \\u2013 \\u062a\\u062d\\u0644\\u064a\\u0644 \\u0627\\u0644\\u0645\\u0634\\u0627\\u0639\\u0631 \\u0628\\u0645\\u0639\\u0627\\u0644\\u062c\\u0629 \\u0627\\u0644\\u0644\\u063a\\u0629 \\u0627\\u0644\\u0637\\u0628\\u064a\\u0639\\u064a\\u0629"]
1	Data Scientist	zeroG – AI in Aviation (Lufthansa Group)	Frankfurt, Germany	Dec 2022 — Present	Lead the innovation, design, and implementation of advanced AI systems to drive customer engagement and strategic business initiatives. Serve as a key resource for Generative and Agentic AI.	["<span class=\\"accent-hl\\">Keynote on Agentic AI</span> with live multi-agent system demo at Data Community Day", "Pioneered first <span class=\\"accent-hl\\">g</span><span class=\\"accent-hl\\">enerative AI 'categories model' </span>for city destination scoring", "Engineered <span class=\\"accent-hl\\">ancillary recommender&nbsp;</span><span>driving<span class=\\"Apple-converted-space\\">&nbsp;</span></span><span><span class=\\"accent-hl\\">3-15% purchase increase</span></span><span><span class=\\"Apple-converted-space\\">&nbsp;</span>across airlines</span>", "Optimised recommender APIs for up to <span class=\\"accent-hl\\">20x performance gain</span>", "Built <span class=\\"accent-hl\\">comprehensive AB testing pipeline</span> from scratch for rigorous model validation"]	1	عالم بيانات	أقود ابتكار وتصميم وتنفيذ أنظمة الذكاء الاصطناعي المتقدمة لتعزيز مشاركة العملاء والمبادرات الاستراتيجية. أعمل كمرجع رئيسي في مجال الذكاء الاصطناعي التوليدي والعملي.	["<strong>\\u0643\\u0644\\u0645\\u0629 \\u0631\\u0626\\u064a\\u0633\\u064a\\u0629 \\u0639\\u0646 \\u0627\\u0644\\u0630\\u0643\\u0627\\u0621 \\u0627\\u0644\\u0627\\u0635\\u0637\\u0646\\u0627\\u0639\\u064a \\u0627\\u0644\\u0639\\u0645\\u0644\\u064a</strong> \\u0645\\u0639 \\u0639\\u0631\\u0636 \\u062d\\u064a \\u0644\\u0646\\u0638\\u0627\\u0645 \\u0645\\u062a\\u0639\\u062f\\u062f \\u0627\\u0644\\u0648\\u0643\\u0644\\u0627\\u0621 \\u0641\\u064a \\u064a\\u0648\\u0645 \\u0645\\u062c\\u062a\\u0645\\u0639 \\u0627\\u0644\\u0628\\u064a\\u0627\\u0646\\u0627\\u062a", "\\u0631\\u0627\\u0626\\u062f \\u0623\\u0648\\u0644 <strong>\\u0646\\u0645\\u0648\\u0630\\u062c \\u0641\\u0626\\u0627\\u062a \\u0628\\u0627\\u0644\\u0630\\u0643\\u0627\\u0621 \\u0627\\u0644\\u0627\\u0635\\u0637\\u0646\\u0627\\u0639\\u064a \\u0627\\u0644\\u062a\\u0648\\u0644\\u064a\\u062f\\u064a</strong> \\u0644\\u062a\\u0642\\u064a\\u064a\\u0645 \\u0648\\u062c\\u0647\\u0627\\u062a \\u0627\\u0644\\u0645\\u062f\\u0646", "\\u0628\\u0646\\u0627\\u0621 <strong>\\u0646\\u0638\\u0627\\u0645 \\u062a\\u0648\\u0635\\u064a\\u0629 \\u0625\\u0636\\u0627\\u0641\\u064a</strong> \\u064a\\u0631\\u0641\\u0639 \\u0645\\u0639\\u062f\\u0644 \\u0627\\u0644\\u0634\\u0631\\u0627\\u0621 \\u0628\\u0646\\u0633\\u0628\\u0629 <strong>3-15%</strong> \\u0639\\u0628\\u0631 \\u0634\\u0631\\u0643\\u0627\\u062a \\u0627\\u0644\\u0637\\u064a\\u0631\\u0627\\u0646", "\\u062a\\u062d\\u0633\\u064a\\u0646 \\u0623\\u062f\\u0627\\u0621 \\u0648\\u0627\\u062c\\u0647\\u0627\\u062a \\u0628\\u0631\\u0645\\u062c\\u0629 \\u0627\\u0644\\u062a\\u0637\\u0628\\u064a\\u0642\\u0627\\u062a \\u0628\\u0645\\u0639\\u062f\\u0644 \\u064a\\u0635\\u0644 \\u0625\\u0644\\u0649 <strong>20 \\u0636\\u0639\\u0641\\u0627\\u064b</strong>", "\\u0625\\u0646\\u0634\\u0627\\u0621 \\u0645\\u0646\\u0638\\u0648\\u0645\\u0629 <strong>\\u0627\\u062e\\u062a\\u0628\\u0627\\u0631 AB</strong> \\u0634\\u0627\\u0645\\u0644\\u0629 \\u0645\\u0646 \\u0627\\u0644\\u0635\\u0641\\u0631 \\u0644\\u0644\\u062a\\u062d\\u0642\\u0642 \\u0627\\u0644\\u0635\\u0627\\u0631\\u0645 \\u0645\\u0646 \\u0627\\u0644\\u0646\\u0645\\u0627\\u0630\\u062c"]
5	BSc Informatics Engineering — AI Major	Arab International University	Damascus, Syria	Sep 2015 — Mar 2021	Thesis: Human Behavior Simulation — a multi-modal AI system combining voice cloning, 3D avatar reconstruction, and deep RL agent training.	["<span class=\\"accent-hl\\">Voice Cloning </span>via Zero-Shot Learning from 5-20s audio samples", "<span class=\\"accent-hl\\">3D Avatar Reconstruction</span> using Facebook's PIFu from a single image", "<span class=\\"accent-hl\\">RL Agent </span>trained to walk in Unity via PPO"]	5	بكالوريوس هندسة المعلوماتية – تخصص ذكاء اصطناعي	الأطروحة: محاكاة السلوك البشري – نظام ذكاء اصطناعي متعدد الوسائط يجمع بين استنساخ الصوت وإعادة بناء الصورة الرمزية ثلاثية الأبعاد وتدريب وكيل التعلم المعزز العميق.	["<span><span class=\\"accent-hl\\">\\u0627\\u0633\\u062a\\u0646\\u0633\\u0627\\u062e \\u0627\\u0644\\u0635\\u0648\\u062a</span></span><span><span class=\\"Apple-converted-space\\">&nbsp;</span>\\u0639\\u0628\\u0631 Zero-Shot Learning \\u0645\\u0646 5-20 \\u062b\\u0627\\u0646\\u064a\\u0629 \\u0635\\u0648\\u062a\\u064a\\u0629</span>", "<span><span class=\\"accent-hl\\">\\u0625\\u0639\\u0627\\u062f\\u0629 \\u0628\\u0646\\u0627\\u0621 \\u0635\\u0648\\u0631\\u0629 \\u0631\\u0645\\u0632\\u064a\\u0629 \\u062b\\u0644\\u0627\\u062b\\u064a\\u0629 \\u0627\\u0644\\u0623\\u0628\\u0639\\u0627\\u062f</span></span><span><span class=\\"Apple-converted-space\\">&nbsp;</span>\\u0628\\u0627\\u0633\\u062a\\u062e\\u062f\\u0627\\u0645 PIFu \\u0645\\u0646 Facebook \\u0645\\u0646 \\u0635\\u0648\\u0631\\u0629 \\u0648\\u0627\\u062d\\u062f\\u0629</span>", "<span><span class=\\"accent-hl\\">\\u0648\\u0643\\u064a\\u0644 \\u0627\\u0644\\u062a\\u0639\\u0644\\u0645 \\u0627\\u0644\\u0645\\u0639\\u0632\\u0632</span></span><span><span class=\\"Apple-converted-space\\">&nbsp;</span>\\u0645\\u064f\\u062f\\u0631\\u064e\\u0651\\u0628 \\u0639\\u0644\\u0649 \\u0627\\u0644\\u0645\\u0634\\u064a \\u0641\\u064a Blender/Unity \\u0639\\u0628\\u0631 PPO</span>"]
2	AI Engineer	Freelance	Remote	Apr 2021 — Oct 2022	Delivered end-to-end AI solutions for diverse clients, managing every stage from scoping to deployment and maintenance.	["<span class=\\"accent-hl\\">'Virtual Patient'</span> simulation for interactive medical training", "Automated <span class=\\"accent-hl\\">Dark Web Auto-Labelling &amp; Classification</span> system"]	2	مهندس ذكاء اصطناعي	تسليم حلول ذكاء اصطناعي متكاملة لعملاء متنوعين، مع إدارة كل مرحلة من تحديد النطاق حتى النشر والصيانة.	["<span>\\u0645\\u062d\\u0627\\u0643\\u0627\\u0629<span class=\\"Apple-converted-space\\">&nbsp;</span></span><span><span class=\\"accent-hl\\">'\\u0627\\u0644\\u0645\\u0631\\u064a\\u0636 \\u0627\\u0644\\u0627\\u0641\\u062a\\u0631\\u0627\\u0636\\u064a'</span></span><span><span class=\\"Apple-converted-space\\">&nbsp;</span>\\u0644\\u0644\\u062a\\u062f\\u0631\\u064a\\u0628 \\u0627\\u0644\\u0637\\u0628\\u064a \\u0627\\u0644\\u062a\\u0641\\u0627\\u0639\\u0644\\u064a</span>", "<span>\\u0646\\u0638\\u0627\\u0645 \\u0622\\u0644\\u064a</span><span> </span><span></span><span class=\\"accent-hl\\"><span>\\u0644</span><span>\\u0640</span><span>\\u0627\\u0644\\u062a\\u0635\\u0646\\u064a\\u0641 \\u0648\\u0627\\u0644\\u0648\\u0633\\u0645 \\u0627\\u0644\\u062a\\u0644\\u0642\\u0627\\u0626\\u064a \\u0644\\u0644\\u0648\\u064a\\u0628 \\u0627\\u0644\\u0645\\u0638\\u0644\\u0645</span></span><span></span><span></span><span></span><span></span>"]
\.


--
-- Data for Name: impact_cards; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.impact_cards (id, icon, value, prefix, suffix, description, sort_order, description_ar) FROM stdin;
1	&#9883;	15		%	Ancillary purchase lift across airline partners	1	زيادة في مشتريات الإضافات عبر شركاء شركات الطيران
2	&#9889;	20		x	Recommender API speedup for real-time scoring	2	تسريع واجهة برمجة الموصيات للتقييم الفوري
3	&#9992;	6		+	Airlines served with personalized recommendations	3	شركات طيران تخدمها توصيات مخصصة
4	&#9733;	2			Keynote presenter at the biggest LHG data event	4	متحدث رئيسي في أكبر حدث بيانات في مجموعة لوفتهانزا
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
292	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-04 12:59:49.457097
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
150	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-01 04:13:57.925326
151	/favicon.ico		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:01.328622
152	/apple-touch-icon-precomposed.png		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:01.396431
153	/apple-touch-icon-120x120.png		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:01.635947
154	/apple-touch-icon-precomposed.png		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:01.71917
155	/apple-touch-icon.png		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:01.788093
156	/favicon.ico		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:01.856969
157	/apple-touch-icon-120x120-precomposed.png		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:01.965372
158	/apple-touch-icon-120x120.png		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:02.042741
159	/apple-touch-icon-precomposed.png		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:02.10717
160	/apple-touch-icon.png		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:02.147408
161	/favicon.ico		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:21:02.180845
162	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:22:05.684308
163	/favicon.ico		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:22:07.076755
164	/apple-touch-icon.png		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:22:07.153841
165	/apple-touch-icon-precomposed.png		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-01 15:22:07.154337
166	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 04:04:31.678115
167	/.well-known/traffic-advice		Chrome Privacy Preserving Prefetch Proxy	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 08:50:05.424412
168	/.well-known/traffic-advice		Chrome Privacy Preserving Prefetch Proxy	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 08:50:05.587587
169	/	https://www.google.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 08:50:05.684686
170	/	https://www.google.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 08:53:29.971888
171	/	https://www.google.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 08:53:30.03866
172	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 08:56:52.221445
173	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 10:24:59.454217
174	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 10:26:53.074371
175	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:28:10.330779
176	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:28:35.296457
177	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:29:33.141548
178	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:30:21.89344
179	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:34:19.059061
180	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 10:34:49.804353
181	/	https://mohamed-maa-albared-portfolio.onrender.com	Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 10:34:49.988997
182	/privacy	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:35:59.027497
183	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:41:51.26152
184	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:41:51.308542
185	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:42:28.543137
186	/case-study/1	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:44:14.905382
187	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:44:39.744278
188	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:45:13.745875
189	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:47:03.139065
293	/	https://mohamed-maa-albared-portfolio.onrender.com	Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-04 12:59:49.647069
190	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:47:33.720113
191	/blog/agentic-ai-revolution-autonomous-reasoners	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:47:56.776394
192	/blog/recommendation-systems-aviation-engineering-serendipity		Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:48:25.046925
193	/blog/agentic-ai-revolution-autonomous-reasoners	https://mohamed-maa-albared-portfolio.onrender.com/en/blog/agentic-ai-revolution-autonomous-reasoners	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:48:31.007403
194	/blog/agentic-ai-revolution-autonomous-reasoners	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog/agentic-ai-revolution-autonomous-reasoners	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:48:44.26792
195	/blog	https://mohamed-maa-albared-portfolio.onrender.com/en/blog/agentic-ai-revolution-autonomous-reasoners	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 10:49:12.168901
196	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 11:27:30.634645
197	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:27:54.052844
198	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:28:02.580073
199	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:28:20.321219
200	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/admin/login	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:29:08.096604
201	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 11:45:04.819949
202	/	https://mohamed-maa-albared-portfolio.onrender.com	Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 11:45:05.003318
203	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:45:33.561634
204	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:53:20.700924
205	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:53:24.717695
206	/case-study/1	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:54:59.086164
207	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/case-study/1	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:56:18.743566
208	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:57:17.513167
209	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog/architecture-of-thought-neuroscience-ai-agents	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:57:54.938432
210	/blog	https://mohamed-maa-albared-portfolio.onrender.com/en/blog/architecture-of-thought-neuroscience-ai-agents	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:58:04.702324
211	/	https://mohamed-maa-albared-portfolio.onrender.com/en/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:58:09.689332
212	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:58:16.860401
213	/privacy	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:59:52.300844
214	/privacy	https://mohamed-maa-albared-portfolio.onrender.com/ar/privacy	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 11:59:58.64895
215	/	https://mohamed-maa-albared-portfolio.onrender.com/en/privacy	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:00:01.334746
216	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:00:13.771453
217	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:02:34.916802
218	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:03:37.537377
219	/blog	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:04:58.821087
220	/blog/recommendation-systems-aviation-engineering-serendipity	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:05:04.133727
221	/blog/recommendation-systems-aviation-engineering-serendipity	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog/recommendation-systems-aviation-engineering-serendipity	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:05:36.359634
222	/	https://mohamed-maa-albared-portfolio.onrender.com/en/blog/recommendation-systems-aviation-engineering-serendipity	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:05:51.443795
223	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:07:44.865427
224	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:08:56.283765
226	/		Mozilla/5.0 (compatible; Google-InspectionTool/1.0;)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 12:10:52.465797
225	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:09:06.737845
227	/		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; Google-InspectionTool/1.0;)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-02 12:10:52.465797
229	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:11:40.06223
230	/	https://mohamed-maa-albared-portfolio.onrender.com/de/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:12:04.401589
231	/de		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:12:12.256593
232	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/de	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:12:15.944829
228	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:11:36.528998
233	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:29:40.859123
234	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/experience/5/edit	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:32:02.682373
235	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:33:34.494873
236	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-02 12:35:15.106964
237	/project/5		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 00:07:04.34836
238	/project/7		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 00:42:36.137052
239	/project/4		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:09:56.725494
240	/blog		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:14:24.353092
241	/project/4		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:16:20.508905
242	/blog/neural-canvas-art-neuroscience-ai		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:20:11.91045
243	/privacy		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:23:01.379523
244	/project/1		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:27:05.171692
245	/case-study/1		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:29:34.731036
246	/project/6		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:30:17.687745
247	/project/1		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:31:52.794976
248	/project/9		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:37:13.840457
249	/project/12		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 02:51:36.116314
250	/project/8		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 03:23:58.801979
251	/project/4		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 03:37:47.205534
252	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 04:05:25.94458
253	/	https://mohamed-maa-albared-portfolio.onrender.com	Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 04:05:26.123486
254	/blog		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 04:10:38.014603
255	/blog/architecture-of-thought-neuroscience-ai-agents		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:40:42.400441
256	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:40:59.964215
257	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:00.10204
258	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:05.889338
259	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:06.45231
260	/privacy	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:09.617228
263	/blog	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:15.165301
264	/case-study/1	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:17.513356
267	/privacy	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:21.281358
268	/blog/recommendation-systems-aviation-engineering-serendipity	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog/agentic-ai-revolution-autonomous-reasoners	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:21.498593
272	/blog/neural-canvas-art-neuroscience-ai	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:25.938574
273	/blog	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:26.196509
277	/case-study/1	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:27.651899
278	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:27.849757
279	/blog/recommendation-systems-aviation-engineering-serendipity	https://mohamed-maa-albared-portfolio.onrender.com/en/blog	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:28.566249
280	/blog	https://mohamed-maa-albared-portfolio.onrender.com/en/blog	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:29.543368
261	/blog/agentic-ai-revolution-autonomous-reasoners	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:12.491018
262	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:12.577094
265	/blog	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:19.059687
266	/blog/neural-canvas-art-neuroscience-ai	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:19.634143
269	/blog	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:23.274896
270	/blog/agentic-ai-revolution-autonomous-reasoners	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:24.681054
271	/blog	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:24.816905
274	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:26.540536
275	/	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:27.036093
276	/blog	https://mohamed-maa-albared-portfolio.onrender.com/en/blog	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:27.474747
281	/blog	https://mohamed-maa-albared-portfolio.onrender.com/en/blog	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 05:41:30.408996
282	/blog		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 06:45:09.11116
283	/blog/architecture-of-thought-neuroscience-ai-agents		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 06:45:12.032025
284	/blog/recommendation-systems-aviation-engineering-serendipity		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 07:53:02.822548
285	/		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 10:06:18.158678
286	/blog/recommendation-systems-aviation-engineering-serendipity		Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; GoogleOther)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 10:33:12.637245
287	/blog/None		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/23.0.912.77 Safari/535.7	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 14:39:36.588706
288	/blog	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 14:44:45.282532
289	/blog	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog?category={search_term_string}	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 14:44:51.190362
290	/blog	https://mohamed-maa-albared-portfolio.onrender.com/en/blog?category={search_term_string}	Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.3; +https://openai.com/gptbot)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-03 14:44:53.787009
291	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-04 03:59:44.938683
294	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:00:00.448382
295	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:00:15.411667
296	/case-study/1	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:01:10.536287
297	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:01:19.30776
298	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:02:57.543123
299	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-04 13:11:06.534169
300	/	https://mohamed-maa-albared-portfolio.onrender.com	Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-04 13:11:06.717459
301	/		Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/144.0.7559.95 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:18:39.163101
302	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-04 13:36:45.6283
303	/	https://mohamed-maa-albared-portfolio.onrender.com	Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-04 13:36:45.828477
304	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/skill-cluster/4/edit	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:40:49.169379
305	/	https://mohamed-maa-albared-portfolio.onrender.com/admin/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:41:32.124911
306	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/static/images/profile.png	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:42:13.016271
307	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-04 13:45:41.465631
308	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:08.391381
311	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:08.782599
313	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:08.875973
318	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.571419
323	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.677571
324	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.68622
325	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.790764
326	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.872629
327	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.877623
332	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.078636
333	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.271751
335	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.375943
337	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.571877
338	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.576068
340	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.686031
342	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.877419
343	/blog/architecture-of-thought-neuroscience-ai-agents	https://mohamed-maa-albared-portfolio.onrender.com/ar/blog/architecture-of-thought-neuroscience-ai-agents	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-05 15:51:00.015355
344	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/144.0.7559.95 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-05 16:16:30.547074
345	/apple-touch-icon-precomposed.png		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-06 20:49:49.651127
346	/favicon.ico		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-06 20:49:49.747963
347	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-08 04:06:31.827952
348	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-08 12:17:14.715668
349	/	https://mohamed-maa-albared-portfolio.onrender.com/ar/	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-08 12:19:45.564325
350	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-08 16:57:29.966143
351	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.054649
353	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.26036
355	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.458025
357	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.659076
359	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.857807
361	/favicon.ico		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-11 20:02:31.011546
362	/		okhttp/5.3.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-11 20:22:08.109206
363	/		okhttp/5.3.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-11 20:22:08.305256
364	/		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/138.0.7204.23 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-11 20:22:57.000904
365	/		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/138.0.7204.23 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-11 20:22:57.12601
366	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/138.0.7204.23 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-11 20:22:58.943812
309	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:08.672294
310	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:08.773275
312	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:08.781812
314	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:08.882334
315	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.075487
316	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.172915
317	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.471916
319	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.572118
320	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.578797
321	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.584493
322	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.671886
328	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.977628
329	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:09.983506
330	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.071785
331	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.075757
334	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.275933
336	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.376729
339	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.675743
341	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-05 09:08:10.782741
352	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.154587
354	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.359428
356	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.560852
358	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.673797
360	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-09 02:43:30.861529
367	/		Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/144.0.7559.95 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-11 20:23:21.730603
368	/		Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/144.0.7559.95 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-11 20:23:22.169787
369	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/	Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/144.0.7559.95 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-13 13:15:18.820386
370	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 04:29:06.930781
371	/	https://mohamed-maa-albared-portfolio.onrender.com	Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 04:29:07.472618
372	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:41.263286
385	/		Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/144.0.7559.95 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-16 09:10:33.970064
386	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-17 09:54:14.855789
387	/	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-17 09:54:15.52811
388	/		Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/144.0.7559.95 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-17 10:29:48.004366
389	/favicon.ico		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-20 17:48:10.353111
391	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.4 facebookexternalhit/1.1 Facebot Twitterbot/1.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-20 17:48:10.401991
392	/		Mozilla/5.0 (compatible; Google-Site-Verification/1.0)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 02:24:34.668055
393	/		Mozilla/5.0 (compatible; Google-Site-Verification/1.0)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 02:24:35.026991
394	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 04:13:42.186333
396	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:33.65777
398	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:33.866811
399	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:34.064377
401	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:34.164188
402	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:34.254481
405	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:34.452155
407	/apple-touch-icon-precomposed.png		NetworkingExtension/8623.2.7.110.1 Network/5569.82.5 iOS/26.3.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-25 18:33:32.128267
408	/		Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-29 04:33:11.434597
409	/	https://mohamed-maa-albared-portfolio.onrender.com	Go-http-client/2.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-29 04:33:11.636813
410	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:08.362852
411	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:08.826435
423	/favicon.ico		NetworkingExtension/8623.2.7.110.1 Network/5569.82.5 iOS/26.3.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-04-02 19:21:15.802877
424	/apple-touch-icon-precomposed.png		NetworkingExtension/8623.2.7.110.1 Network/5569.82.5 iOS/26.3.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-04-02 19:21:16.011262
425	/		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-04-03 07:52:11.717999
426	/		okhttp/5.3.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-04-03 08:04:04.340587
427	/favicon.ico		okhttp/5.3.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-04-03 08:04:04.741101
428	/favicon.png		okhttp/5.3.0	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-04-03 08:04:05.036504
429	/		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/138.0.7204.23 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-04-03 08:05:05.950413
430	/		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/138.0.7204.23 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-04-03 08:05:06.112205
431	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/138.0.7204.23 Safari/537.36	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-04-03 08:05:07.597004
432	/favicon.ico	https://mohamed-maa-albared-portfolio.onrender.com/en/	Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3 Mobile/15E148 Safari/604.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-04-03 19:39:45.69177
373	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:41.864966
375	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:42.563396
376	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:42.85928
378	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:42.877546
381	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:43.062591
382	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:43.163512
384	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:43.460249
390	/apple-touch-icon.png		NetworkingExtension/8623.2.7.10.4 Network/5569.82.5 iOS/26.3.1	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7	en-US	2026-03-20 17:48:10.352269
395	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:33.656874
397	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:33.857585
400	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:34.151363
403	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:34.262259
404	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:34.35589
406	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-22 21:32:34.551162
412	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:09.759881
417	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:10.552439
420	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:10.6618
374	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:42.06293
377	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:42.862754
379	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:42.970547
380	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:43.059992
383	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-15 17:45:43.167175
413	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:09.86183
414	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:09.96061
415	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:10.059371
416	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:10.354945
418	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:10.552392
419	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:10.569925
421	/blog		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:10.665342
422	/		Mozilla/5.0 (compatible)	3b4c59ff876ab53c12b9c65e5b1bc3bbb0db515e8876687222bd29573d2a8ee7		2026-03-30 14:28:10.75961
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects (id, title, description, short_description, image_url, demo_url, github_url, technologies, category, year, client, created_at, updated_at, featured, case_study, metrics, challenge, approach, results, has_case_study, sort_order, title_ar, short_description_ar, description_ar, challenge_ar, approach_ar, results_ar, case_study_ar) FROM stdin;
1	Multi-Agent Voice System	Designed and built a live, multi-agent system demo presented as a keynote at the Lufthansa Group Data Community Day 2025. The system processes voice commands, transcribes them, and uses an LLM orchestrator to delegate tasks to specialised search and data analysis agents — solving complex business queries in real-time.	Voice-activated autonomous business analysis.	\N	\N	\N	Python,LLM Orchestration,Whisper,Azure OpenAI,Multi-Agent Systems	genai	2025	Lufthansa Group	2026-02-23 11:56:27.776374	2026-03-02 11:43:26.296372	t	\N	[{"value": "2nd", "label": "Consecutive Year Keynoting"}, {"value": "Live", "label": "Working Demo on Stage"}, {"value": "Voice", "label": "Enabled Multi-Agent System"}, {"value": "3", "label": "Specialised Agents"}]	<p>The Lufthansa Group Data Community Day is the biggest and most sought-after annual data event in the Group. I was tasked with representing zeroG by delivering an advanced presentation on Agentic AI and Multi-Agent Systems. The challenge: go beyond slides and build a <strong>working, voice-activated multi-agent system</strong> that could accept natural voice commands, reason about the intent, and coordinate multiple specialised agents to produce actionable business insights — all live on stage with zero tolerance for failure.</p><p>Traditional chatbots fall short here — they can't decompose complex queries, delegate subtasks, or synthesise information from multiple sources autonomously.</p>	<p>The architecture follows a <strong>hierarchical orchestration pattern</strong>:</p><ul><li><strong>Voice Layer:</strong> Real-time voice transcription converts spoken commands into text</li><li><strong>Orchestrator Agent:</strong> An LLM-powered coordinator that parses intent, decomposes the query into subtasks, and selects the appropriate specialist agent</li><li><strong>Search Agent:</strong> Retrieves relevant information from knowledge bases for research tasks</li><li><strong>Data Analysis Agent:</strong> Handles data queries, computes KPIs, and generates insights for business analysis</li></ul><p>The presentation, titled "LLMs: From Chatty Cathy to Autonomous Agents," walked the audience through the evolution of AI from simple chatbots to autonomous reasoning systems, culminating in the live demo.</p>	<p>The live demo at Data Community Day 2025 was delivered successfully:</p><ul><li>Successfully demonstrated <strong>autonomous task delegation</strong> across specialised agents solving a business query in real-time</li><li>The presentation <strong>sparked significant discussions</strong> about agentic AI adoption across the organisation</li><li>Demonstrated zeroG's <strong>cutting-edge expertise</strong> in autonomous AI systems</li><li>This was my <strong>second consecutive year</strong> keynoting at Data Community Day, reinforcing thought leadership</li></ul>	t	1	نظام صوتي متعدد الوكلاء	تحليل أعمال مستقل يعمل بالصوت.	تصميم وبناء عرض توضيحي حي لنظام متعدد الوكلاء قُدِّم كخطاب رئيسي في يوم مجتمع بيانات مجموعة لوفتهانزا 2025. يعالج النظام الأوامر الصوتية ويحوّلها إلى نص، ويستخدم منسّق LLM لتفويض المهام إلى وكلاء البحث وتحليل البيانات المتخصصين — لحل استفسارات الأعمال المعقدة في الوقت الحقيقي.	<p>يُعدّ يوم مجتمع بيانات مجموعة لوفتهانزا أكبر حدث بيانات سنوي في المجموعة. أُسنِد إليّ تمثيل zeroG من خلال تقديم عرض متقدم عن الذكاء الاصطناعي العملي وأنظمة الوكلاء المتعددة. التحدي: تجاوز الشرائح وبناء <strong>نظام متعدد الوكلاء يعمل بالصوت</strong> قادر على قبول الأوامر الصوتية الطبيعية والاستدلال على النية وتنسيق وكلاء متخصصين متعددين لإنتاج رؤى أعمال قابلة للتنفيذ — كل هذا مباشرة على المسرح بلا هامش للفشل.</p><p>روبوتات الدردشة التقليدية تقصر هنا — إذ لا تستطيع تفكيك الاستفسارات المعقدة أو تفويض المهام الفرعية أو دمج المعلومات من مصادر متعددة باستقلالية.</p>	<p>تتبع البنية <strong>نمط التنسيق الهرمي</strong>:</p><ul><li><strong>طبقة الصوت:</strong> تحويل الأوامر الصوتية إلى نص في الوقت الحقيقي</li><li><strong>وكيل المنسّق:</strong> منسّق يعمل بـ LLM يحلل النية ويفكك الاستفسار إلى مهام فرعية ويختار الوكيل المتخصص المناسب</li><li><strong>وكيل البحث:</strong> استرجاع المعلومات ذات الصلة من قواعد المعرفة للمهام البحثية</li><li><strong>وكيل تحليل البيانات:</strong> معالجة استفسارات البيانات وحساب مؤشرات الأداء وتوليد الرؤى التحليلية</li></ul><p>قدّم العرض، المعنون «نماذج اللغة الكبيرة: من المحادثة إلى الوكلاء المستقلين»، للجمهور مسيرة تطور الذكاء الاصطناعي من روبوتات الدردشة البسيطة إلى أنظمة الاستدلال المستقلة.</p>	<p>نُفِّذ العرض الحي في يوم مجتمع البيانات 2025 بنجاح:</p><ul><li>إثبات ناجح لـ<strong>تفويض المهام المستقل</strong> عبر وكلاء متخصصين لحل استفسار أعمال في الوقت الحقيقي</li><li>أشعل العرض <strong>نقاشات واسعة</strong> حول تبني الذكاء الاصطناعي العملي في المنظمة</li><li>إثبات <strong>الخبرة المتطورة</strong> لـzeroG في أنظمة الذكاء الاصطناعي المستقلة</li><li>كان هذا <strong>عامي الثاني على التوالي</strong> في تقديم الخطاب الرئيسي، مما يعزز ريادة الفكر</li></ul>	\N
4	AB Testing Framework	Led research and development of a comprehensive, generalised AB testing framework. Includes covariate balance checking, ATE analysis, and a sophisticated CATE framework with five meta-learners, SHAP-based customer archetype discovery, and automated dual-reporting (technical and stakeholder). This pipeline became the foundation for a newly created independent Performance Measurement team at the client.	Comprehensive experimentation pipeline with causal inference.	\N	\N	\N	Python,Causal Inference,SHAP,Meta-Learners,Statistical Testing	recsys	2024	Lufthansa Group	2026-02-23 11:56:27.77903	2026-03-02 11:43:26.299875	f	\N	\N	\N	\N	\N	f	4	إطار اختبار AB	منظومة تجريب شاملة مع الاستدلال السببي.	قيادة البحث والتطوير لإطار اختبار AB شامل ومعمّم. يتضمن فحص توازن المتغيرات المشتركة، وتحليل ATE، وإطار CATE متطور مع خمسة متعلّمات تلوية، واكتشاف نماذج العملاء القائم على SHAP، وتقارير مزدوجة آلية (تقنية وللمساهمين).	\N	\N	\N	\N
5	Human Behavior Simulation	Master's thesis combining three AI modalities: Zero-Shot voice cloning, 3D avatar reconstruction (PIFu), and deep RL agent training (PPO).	Multi-modal AI: voice cloning + 3D avatar + RL agent.	\N	\N	\N	Python,TensorFlow,Blender,Unity,C#,PPO	rl cv	2021	Arab International University	2026-02-23 11:56:27.779034	2026-03-02 11:43:26.370617	f	\N	\N	\N	\N	\N	f	5	محاكاة السلوك البشري	ذكاء اصطناعي متعدد الوسائط: استنساخ صوت + صورة رمزية ثلاثية الأبعاد + وكيل RL.	أطروحة الماجستير تجمع بين ثلاثة وسائط للذكاء الاصطناعي: استنساخ الصوت بـZero-Shot، وإعادة بناء الصورة الرمزية ثلاثية الأبعاد (PIFu)، وتدريب وكيل التعلم المعزز العميق (PPO).	\N	\N	\N	\N
6	Virtual Patient Simulation	Developed an AI-powered 'Virtual Patient' simulation for interactive clinical training.	Interactive AI patient for medical training scenarios.	\N	\N	\N	Python,NLP,SGD,Classification,Flask	nlp	2022	Freelance Client	2026-02-23 11:56:27.779035	2026-03-02 11:43:26.37208	f	\N	\N	\N	\N	\N	f	6	محاكاة المريض الافتراضي	مريض ذكاء اصطناعي تفاعلي لسيناريوهات التدريب الطبي.	تطوير محاكاة 'مريض افتراضي' مدعومة بالذكاء الاصطناعي للتدريب السريري التفاعلي.	\N	\N	\N	\N
7	Dark Web Auto-Labelling	Built an automated system for scraping, labelling, and classifying dark web content using NLP-based text classification pipelines.	Automated classification of dark web content.	\N	\N	\N	Python,Scikit-Learn,BeautifulSoup,Selenium,NLP	nlp	2022	Freelance Client	2026-02-23 11:56:27.779036	2026-03-02 11:43:26.373629	f	\N	\N	\N	\N	\N	f	7	الوسم التلقائي للويب المظلم	تصنيف آلي لمحتوى الويب المظلم.	بناء نظام آلي لجمع ووسم وتصنيف محتوى الويب المظلم باستخدام منظومات تصنيف النصوص المعتمدة على معالجة اللغة الطبيعية.	\N	\N	\N	\N
8	Emotion Prediction from Voice	Deep learning model predicting human emotions (calm, happy, sad, angry, fearful, surprised, disgusted) from audio files using Inception networks on mel-spectrograms.	Deep learning classifier for vocal emotion detection.	\N	\N	\N	Python,TensorFlow,Keras,Inception,Mel-Spectrogram	cv	2021	Damascus Start-Up	2026-02-23 11:56:27.779037	2026-03-02 11:43:26.374969	f	\N	\N	\N	\N	\N	f	8	التنبؤ بالمشاعر من الصوت	مصنّف تعلم عميق للكشف عن المشاعر الصوتية.	نموذج تعلم عميق يتنبأ بالمشاعر البشرية (هادئ، سعيد، حزين، غاضب، خائف، مفاجأ، مشمئز) من الملفات الصوتية باستخدام شبكات Inception على الطيف الصوتي.	\N	\N	\N	\N
9	Arabic Tweets Classifier	Kaggle competition for classifying Arabic tweets into positive, negative, and neutral sentiment classes. Achieved 75.9% accuracy using BERT with extensive Arabic language processing.	Sentiment analysis for Arabic social media text.	\N	\N	\N	Python,BERT,Arabic NLP,Kaggle	nlp	2021	Damascus Start-Up	2026-02-23 11:56:27.779038	2026-03-02 11:43:26.376281	f	\N	\N	\N	\N	\N	f	9	مصنّف التغريدات العربية	تحليل المشاعر لنصوص وسائل التواصل الاجتماعي العربية.	مسابقة Kaggle لتصنيف التغريدات العربية إلى فئات المشاعر الإيجابية والسلبية والمحايدة. حققت دقة 75.9% باستخدام BERT مع معالجة شاملة للغة العربية.	\N	\N	\N	\N
10	Forex Forecasting (JPY/CAD)	Predicting JPY/CAD exchange rates using 20 years of scraped economic data from multiple websites and Reuters news. Combined macroeconomic features from Japan, Canada, and the USA with deep neural networks for prediction.	Time-series model for foreign exchange prediction.	\N	\N	\N	Python,TensorFlow,Web Scraping,Reuters NLP,Deep NN	nlp	2020	Damascus Start-Up	2026-02-23 11:56:27.77904	2026-03-02 11:43:26.378064	f	\N	\N	\N	\N	\N	f	10	التنبؤ بأسعار صرف العملات (JPY/CAD)	نموذج سلاسل زمنية للتنبؤ بأسعار الصرف.	التنبؤ بأسعار صرف JPY/CAD باستخدام 20 عاماً من البيانات الاقتصادية المجمّعة من مواقع متعددة وأخبار رويترز. دمج المؤشرات الاقتصادية الكلية من اليابان وكندا والولايات المتحدة مع الشبكات العصبية العميقة للتنبؤ.	\N	\N	\N	\N
11	RAG Pipeline with Smart Segmentation	RAG pipeline with smart document segmentation inspired by Anthropic's research, dynamically chunking documents based on semantic boundaries.	Retrieval-Augmented Generation with semantic chunking.	\N	\N	\N	Python,LangChain,FAISS,Azure OpenAI	genai	2024	Personal Project	2026-02-23 11:56:27.779041	2026-03-02 11:43:26.379397	f	\N	\N	\N	\N	\N	f	11	منظومة RAG مع التجزئة الذكية	توليد معزز بالاسترجاع مع التقسيم الدلالي للنصوص.	منظومة RAG مع تجزئة ذكية للوثائق مستوحاة من أبحاث Anthropic، تقسّم الوثائق ديناميكياً بناءً على الحدود الدلالية.	\N	\N	\N	\N
12	AI Search & Reasoning Agents	Multi-step reasoning AI agents with source credibility assessment, chain-of-thought reasoning, and autonomous tool use.	Multi-step reasoning agents inspired by OpenAI O-series.	\N	\N	\N	Python,LangChain,OpenAI,Tool Use,Agents	genai	2024	Personal Project	2026-02-23 11:56:27.779042	2026-03-02 11:43:26.380622	f	\N	\N	\N	\N	\N	f	12	وكلاء البحث والاستدلال بالذكاء الاصطناعي	وكلاء استدلال متعدد الخطوات مستلهمة من OpenAI O-series.	وكلاء ذكاء اصطناعي للاستدلال متعدد الخطوات مع تقييم مصداقية المصادر، والتفاوض الفكري المتسلسل، واستخدام الأدوات باستقلالية.	\N	\N	\N	\N
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
13	hero_label_ar	عالم بيانات &bull; مهندس ذكاء اصطناعي	\N	\N
14	hero_tagline_word1_ar	بناء	\N	\N
15	hero_tagline_word2_ar	الذكاء	\N	\N
16	hero_subtitle_ar	حيث تلتقي الشبكات العصبية بالحدس الإبداعي — نبني أنظمة تستدل وتتعاون وتتصرف.	\N	\N
17	about_bio1_ar	عالم بيانات متمرس بأكثر من <strong>4 سنوات من الخبرة</strong> في تطوير ونشر حلول التعلم الآلي والذكاء الاصطناعي التوليدي في <strong>قطاع الطيران</strong>.	\N	\N
18	about_bio2_ar	سجل موثوق في توليد قيمة تجارية ملموسة من خلال هندسة <strong>أنظمة التوصية</strong>، وتحسين أداء النماذج بما يصل إلى <strong>20 ضعفاً</strong>، ورعاية <strong>أُطر اختبار AB</strong> من الصفر.	\N	\N
19	about_bio3_ar	معترف به كخبير متخصص في <strong>تنسيق نماذج اللغة الكبيرة</strong> و<strong>تصميم الوكلاء المستقلين</strong>، ماهر في ترجمة قدرات الذكاء الاصطناعي المعقدة إلى نتائج تجارية استراتيجية مؤثرة.	\N	\N
\.


--
-- Data for Name: skill_clusters; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.skill_clusters (id, icon, title, tags, sort_order, title_ar, tags_ar) FROM stdin;
1	&#129302;	Generative & Agentic AI	LLM Orchestration, Multi-Agent Systems, Prompt Engineering, RAG Pipelines, Fine-Tuning, LangChain/LangGraph, Semantic Kernel	1	الذكاء الاصطناعي التوليدي والعملي	تنسيق نماذج اللغة، أنظمة متعددة الوكلاء، هندسة الأوامر، خطوط RAG، الضبط الدقيق، LangChain/LangGraph، Semantic Kernel
2	&#129504;	ML & Data Science	Recommendation Systems, NLP/NLU, Classification, Regression, Feature Engineering, A/B Testing, XGBoost, Deep Learning	2	التعلم الآلي وعلم البيانات	أنظمة التوصية، معالجة اللغة الطبيعية، التصنيف، الانحدار، هندسة الميزات، اختبار A/B، XGBoost، التعلم العميق
3	&#128187;	Tech Stack	Python, SQL, Flask, FastAPI, TensorFlow, PyTorch, scikit-learn, Pandas, NumPy, Git, REST APIs	3	المنظومة التقنية	بايثون، SQL، Flask، FastAPI، TensorFlow، PyTorch، scikit-learn، Pandas، NumPy، Git، REST APIs
4	&#9729;	Cloud &amp; MLOps	Azure ML,Docker, CI/CD, MLflow, Databricks	4		
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

SELECT pg_catalog.setval('public.messages_id_seq', 2, true);


--
-- Name: page_visits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.page_visits_id_seq', 432, true);


--
-- Name: projects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_id_seq', 12, true);


--
-- Name: site_config_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.site_config_id_seq', 19, true);


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

\unrestrict 7fsMfOTm97TK2oF9tpDm6A3svNCAfetGc1Ik5UoX3kWoHopracLuKWpHXICgw7t

