--
-- PostgreSQL database dump
--

\restrict tZxHoHP4as05fLMZdqs8sbut86SACFLP1hVxB1Gxebmqsjcb61of2H9vME2nopw

-- Dumped from database version 17.6 (Debian 17.6-1.pgdg13+1)
-- Dumped by pg_dump version 17.6 (Debian 17.6-1.pgdg13+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO admin;

--
-- Name: compounds; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.compounds (
    id integer NOT NULL,
    player_1 integer NOT NULL,
    player_2 integer NOT NULL,
    player_3 integer NOT NULL,
    player_4 integer NOT NULL,
    player_5 integer NOT NULL,
    reserve integer NOT NULL,
    trainer integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.compounds OWNER TO admin;

--
-- Name: compounds_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.compounds_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.compounds_id_seq OWNER TO admin;

--
-- Name: compounds_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.compounds_id_seq OWNED BY public.compounds.id;


--
-- Name: matches; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.matches (
    id integer NOT NULL,
    first_team_id integer NOT NULL,
    second_team_id integer NOT NULL,
    time_match date NOT NULL,
    result_first integer NOT NULL,
    result_second integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.matches OWNER TO admin;

--
-- Name: matches_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.matches_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.matches_id_seq OWNER TO admin;

--
-- Name: matches_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.matches_id_seq OWNED BY public.matches.id;


--
-- Name: players; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.players (
    id integer NOT NULL,
    first_name character varying NOT NULL,
    second_name character varying NOT NULL,
    contacts character varying NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.players OWNER TO admin;

--
-- Name: players_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.players_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.players_id_seq OWNER TO admin;

--
-- Name: players_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.players_id_seq OWNED BY public.players.id;


--
-- Name: teams; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.teams (
    id integer NOT NULL,
    name character varying NOT NULL,
    from_country character varying NOT NULL,
    compound_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.teams OWNER TO admin;

--
-- Name: teams_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.teams_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.teams_id_seq OWNER TO admin;

--
-- Name: teams_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.teams_id_seq OWNED BY public.teams.id;


--
-- Name: trainers; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.trainers (
    id integer NOT NULL,
    first_name character varying NOT NULL,
    second_name character varying NOT NULL,
    contacts character varying NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.trainers OWNER TO admin;

--
-- Name: trainers_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.trainers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.trainers_id_seq OWNER TO admin;

--
-- Name: trainers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.trainers_id_seq OWNED BY public.trainers.id;


--
-- Name: trophies; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.trophies (
    id integer NOT NULL,
    name character varying NOT NULL,
    date date NOT NULL,
    team_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.trophies OWNER TO admin;

--
-- Name: trophies_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.trophies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.trophies_id_seq OWNER TO admin;

--
-- Name: trophies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.trophies_id_seq OWNED BY public.trophies.id;


--
-- Name: compounds id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.compounds ALTER COLUMN id SET DEFAULT nextval('public.compounds_id_seq'::regclass);


--
-- Name: matches id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.matches ALTER COLUMN id SET DEFAULT nextval('public.matches_id_seq'::regclass);


--
-- Name: players id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.players ALTER COLUMN id SET DEFAULT nextval('public.players_id_seq'::regclass);


--
-- Name: teams id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.teams ALTER COLUMN id SET DEFAULT nextval('public.teams_id_seq'::regclass);


--
-- Name: trainers id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.trainers ALTER COLUMN id SET DEFAULT nextval('public.trainers_id_seq'::regclass);


--
-- Name: trophies id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.trophies ALTER COLUMN id SET DEFAULT nextval('public.trophies_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.alembic_version (version_num) FROM stdin;
542784264ea8
\.


--
-- Data for Name: compounds; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.compounds (id, player_1, player_2, player_3, player_4, player_5, reserve, trainer, created_at, updated_at) FROM stdin;
0	0	1	2	3	4	0	2	2025-09-08 16:30:00	2025-09-08 16:30:00
1	5	6	7	8	9	5	0	2025-09-08 16:30:00	2025-09-08 16:30:00
2	10	11	12	13	14	10	1	2025-09-08 16:30:00	2025-09-08 16:30:00
\.


--
-- Data for Name: matches; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.matches (id, first_team_id, second_team_id, time_match, result_first, result_second, created_at, updated_at) FROM stdin;
0	1	2	2025-09-18	1	2	2025-09-08 16:30:00	2025-09-08 16:30:00
1	0	1	2025-09-08	2	0	2025-09-08 16:30:00	2025-09-08 16:30:00
2	0	2	2025-09-08	2	1	2025-09-08 16:30:00	2025-09-08 16:30:00
\.


--
-- Data for Name: players; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.players (id, first_name, second_name, contacts, created_at, updated_at) FROM stdin;
0	Илья	Мулярчук	вфврф	2025-09-08 16:30:00	2025-09-08 16:30:00
1	Денис	Сигитов	фывфывфв	2025-09-08 16:30:00	2025-09-08 16:30:00
2	Магомед	Халиков	фывфвы	2025-09-08 16:30:00	2025-09-08 16:30:00
3	Александр	Филин	ыфвфвы	2025-09-08 16:30:00	2025-09-08 16:30:00
4	Ярослав	Найденов	фывфв	2025-09-08 16:30:00	2025-09-08 16:30:00
5	Иван	Москаленко	фыв	2025-09-08 16:30:00	2025-09-08 16:30:00
6	Даниил	Скутин	фывф	2025-09-08 16:30:00	2025-09-08 16:30:00
7	Матвей	Васюнин	фывф	2025-09-08 16:30:00	2025-09-08 16:30:00
8	Виталий	Мельник	вфвы	2025-09-08 16:30:00	2025-09-08 16:30:00
9	Владислав	Семенов	фывфыв	2025-09-08 16:30:00	2025-09-08 16:30:00
10	Оливер	Лепко	фыв	2025-09-08 16:30:00	2025-09-08 16:30:00
11	Станислав	Поторак	ывф	2025-09-08 16:30:00	2025-09-08 16:30:00
12	Аммар	аль-Ассаф	ыфв	2025-09-08 16:30:00	2025-09-08 16:30:00
13	Андреас	Франк	фывфы	2025-09-08 16:30:00	2025-09-08 16:30:00
14	Цзиньцзюнь	Ву	фывф	2025-09-08 16:30:00	2025-09-08 16:30:00
\.


--
-- Data for Name: teams; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.teams (id, name, from_country, compound_id, created_at, updated_at) FROM stdin;
0	TeamSpirit	Russia	0	2025-09-08 16:30:00	2025-09-08 16:30:00
1	BetBoom	Russia	1	2025-09-08 16:30:00	2025-09-08 16:30:00
2	Falcons	Saudi Arabia	2	2025-09-08 16:30:00	2025-09-08 16:30:00
4	Team Liquid	Netherlands	1	2025-09-18 18:43:54.664941	2025-09-18 22:08:34.515587
5	test	test	1	2025-09-18 19:14:05.399317	2025-09-18 19:14:05.399317
6	test1	test1	2	2025-09-18 19:42:31.971165	2025-09-18 19:42:31.971165
\.


--
-- Data for Name: trainers; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.trainers (id, first_name, second_name, contacts, created_at, updated_at) FROM stdin;
2	Айрат	Газиев	АйратГазиев@gmail.com	2025-09-08 16:30:00	2025-09-08 16:30:00
1	Кертис	Лин	КертисЛин@gmail.com	2025-09-08 16:30:00	2025-09-08 16:30:00
0	Анатолий	Иванов	АнатолийИванов@gmail.com	2025-09-08 16:30:00	2025-09-08 16:30:00
\.


--
-- Data for Name: trophies; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.trophies (id, name, date, team_id, created_at, updated_at) FROM stdin;
0	Aegis TI 2025	2025-09-14	2	2025-09-08 16:30:00	2025-09-08 16:30:00
1	Aegis TI 2024	2024-09-07	1	2025-09-08 16:30:00	2025-09-08 16:30:00
\.


--
-- Name: compounds_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.compounds_id_seq', 1, false);


--
-- Name: matches_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.matches_id_seq', 1, false);


--
-- Name: players_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.players_id_seq', 1, false);


--
-- Name: teams_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.teams_id_seq', 1, true);


--
-- Name: trainers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.trainers_id_seq', 1, false);


--
-- Name: trophies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.trophies_id_seq', 1, false);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: compounds compounds_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.compounds
    ADD CONSTRAINT compounds_pkey PRIMARY KEY (id);


--
-- Name: matches matches_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_pkey PRIMARY KEY (id);


--
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (id);


--
-- Name: teams teams_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_name_key UNIQUE (name);


--
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (id);


--
-- Name: trainers trainers_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.trainers
    ADD CONSTRAINT trainers_pkey PRIMARY KEY (id);


--
-- Name: trophies trophies_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.trophies
    ADD CONSTRAINT trophies_pkey PRIMARY KEY (id);


--
-- Name: compounds compounds_player_1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.compounds
    ADD CONSTRAINT compounds_player_1_fkey FOREIGN KEY (player_1) REFERENCES public.players(id);


--
-- Name: compounds compounds_player_2_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.compounds
    ADD CONSTRAINT compounds_player_2_fkey FOREIGN KEY (player_2) REFERENCES public.players(id);


--
-- Name: compounds compounds_player_3_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.compounds
    ADD CONSTRAINT compounds_player_3_fkey FOREIGN KEY (player_3) REFERENCES public.players(id);


--
-- Name: compounds compounds_player_4_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.compounds
    ADD CONSTRAINT compounds_player_4_fkey FOREIGN KEY (player_4) REFERENCES public.players(id);


--
-- Name: compounds compounds_player_5_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.compounds
    ADD CONSTRAINT compounds_player_5_fkey FOREIGN KEY (player_5) REFERENCES public.players(id);


--
-- Name: compounds compounds_reserve_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.compounds
    ADD CONSTRAINT compounds_reserve_fkey FOREIGN KEY (reserve) REFERENCES public.players(id);


--
-- Name: compounds compounds_trainer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.compounds
    ADD CONSTRAINT compounds_trainer_fkey FOREIGN KEY (trainer) REFERENCES public.trainers(id);


--
-- Name: matches matches_first_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_first_team_id_fkey FOREIGN KEY (first_team_id) REFERENCES public.teams(id);


--
-- Name: matches matches_second_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.matches
    ADD CONSTRAINT matches_second_team_id_fkey FOREIGN KEY (second_team_id) REFERENCES public.teams(id);


--
-- Name: teams teams_compound_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_compound_id_fkey FOREIGN KEY (compound_id) REFERENCES public.compounds(id);


--
-- Name: trophies trophies_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.trophies
    ADD CONSTRAINT trophies_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(id);


--
-- PostgreSQL database dump complete
--

\unrestrict tZxHoHP4as05fLMZdqs8sbut86SACFLP1hVxB1Gxebmqsjcb61of2H9vME2nopw

