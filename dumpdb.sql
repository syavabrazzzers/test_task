--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.6 (Ubuntu 14.6-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cart; Type: TABLE; Schema: public; Owner: tailo
--

CREATE TABLE public.cart (
    id integer NOT NULL,
    user_id integer NOT NULL,
    product_id integer NOT NULL,
    count integer NOT NULL
);


ALTER TABLE public.cart OWNER TO tailo;

--
-- Name: cart_id_seq; Type: SEQUENCE; Schema: public; Owner: tailo
--

CREATE SEQUENCE public.cart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cart_id_seq OWNER TO tailo;

--
-- Name: cart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tailo
--

ALTER SEQUENCE public.cart_id_seq OWNED BY public.cart.id;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: tailo
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying,
    slug character varying NOT NULL,
    image character varying,
    parent integer
);


ALTER TABLE public.categories OWNER TO tailo;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: tailo
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO tailo;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tailo
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: product_images; Type: TABLE; Schema: public; Owner: tailo
--

CREATE TABLE public.product_images (
    id integer NOT NULL,
    product_id integer NOT NULL,
    high_quality character varying,
    medium_quality character varying,
    low_quality character varying
);


ALTER TABLE public.product_images OWNER TO tailo;

--
-- Name: product_images_id_seq; Type: SEQUENCE; Schema: public; Owner: tailo
--

CREATE SEQUENCE public.product_images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_images_id_seq OWNER TO tailo;

--
-- Name: product_images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tailo
--

ALTER SEQUENCE public.product_images_id_seq OWNED BY public.product_images.id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: tailo
--

CREATE TABLE public.products (
    id integer NOT NULL,
    name character varying,
    slug character varying NOT NULL,
    category_id integer NOT NULL,
    price numeric NOT NULL
);


ALTER TABLE public.products OWNER TO tailo;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: tailo
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO tailo;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tailo
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: tailo
--

CREATE TABLE public.users (
    id integer NOT NULL,
    login character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO tailo;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: tailo
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO tailo;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tailo
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: cart id; Type: DEFAULT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.cart ALTER COLUMN id SET DEFAULT nextval('public.cart_id_seq'::regclass);


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: product_images id; Type: DEFAULT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.product_images ALTER COLUMN id SET DEFAULT nextval('public.product_images_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: cart; Type: TABLE DATA; Schema: public; Owner: tailo
--

COPY public.cart (id, user_id, product_id, count) FROM stdin;
2	1	5	1
3	2	4	1
10	1	6	2
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: tailo
--

COPY public.categories (id, name, slug, image, parent) FROM stdin;
27	vegetables	vegetables	\N	\N
28	cucmber	cucmber	\N	27
35	qaz	qaz	\N	27
36	zaq	zaq	\N	\N
37	stringasd	stringasd	1688920411.4773889.png	27
33	string	dfdfh	\N	29
29	potato		\N	27
34	123	12345	\N	\N
38	rebb	rebs	1688921503.4186392.png	27
\.


--
-- Data for Name: product_images; Type: TABLE DATA; Schema: public; Owner: tailo
--

COPY public.product_images (id, product_id, high_quality, medium_quality, low_quality) FROM stdin;
2	4	asd	zxc	qwe
3	5	asd	zxc	qwe
4	6	asd	zxc	qwe
5	7	high_1688928939.2726853.png	medium_1688928939.2726853.png	low_1688928939.2726853.png
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: tailo
--

COPY public.products (id, name, slug, category_id, price) FROM stdin;
4	asd	asd	28	111
5	zxc	zxc	29	222
6	qwe	qwe	27	333
7	string222	string222	27	0.2
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: tailo
--

COPY public.users (id, login, password) FROM stdin;
1	string	b45cffe084dd3d20d928bee85e7b0f21
2	user1	e10adc3949ba59abbe56e057f20f883e
3	user2	e10adc3949ba59abbe56e057f20f883e
8	tailo	$2b$12$CML.JqpeyR8/Dyxumld6OesnB.3Bgbfx1eQBkN6mGI5bLgzoxnzJa
\.


--
-- Name: cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tailo
--

SELECT pg_catalog.setval('public.cart_id_seq', 11, true);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tailo
--

SELECT pg_catalog.setval('public.categories_id_seq', 38, true);


--
-- Name: product_images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tailo
--

SELECT pg_catalog.setval('public.product_images_id_seq', 5, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tailo
--

SELECT pg_catalog.setval('public.products_id_seq', 7, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tailo
--

SELECT pg_catalog.setval('public.users_id_seq', 8, true);


--
-- Name: cart cart_pk; Type: CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_pk PRIMARY KEY (id);


--
-- Name: cart cart_un; Type: CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_un UNIQUE (user_id, product_id);


--
-- Name: categories categories_pk; Type: CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pk PRIMARY KEY (id);


--
-- Name: categories categories_un; Type: CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_un UNIQUE (slug);


--
-- Name: product_images product_images_pk; Type: CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.product_images
    ADD CONSTRAINT product_images_pk PRIMARY KEY (id);


--
-- Name: products products_pk; Type: CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pk PRIMARY KEY (id);


--
-- Name: products products_un; Type: CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_un UNIQUE (slug);


--
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- Name: users users_un; Type: CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_un UNIQUE (login);


--
-- Name: cart_user_id_idx; Type: INDEX; Schema: public; Owner: tailo
--

CREATE INDEX cart_user_id_idx ON public.cart USING btree (user_id);


--
-- Name: cart cart_fk; Type: FK CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: cart cart_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_fk_1 FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: categories categories_fk; Type: FK CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_fk FOREIGN KEY (parent) REFERENCES public.categories(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: product_images product_images_fk; Type: FK CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.product_images
    ADD CONSTRAINT product_images_fk FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: products products_fk; Type: FK CONSTRAINT; Schema: public; Owner: tailo
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_fk FOREIGN KEY (category_id) REFERENCES public.categories(id) ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--

