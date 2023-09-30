-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Getting the description of the crime from crime scene reports data
SELECT description FROM crime_scene_reports WHERE year=2021 AND month=7 AND day=28 AND street = "Humphrey Street";

-- Since description mentions that interviews where conducted on three witnesses, we are going to check the interview data for more information
-- Get names and transcripts of the witnesses
SELECT name, transcript FROM interviews WHERE month=7 AND day=28 AND year=2021 AND transcript LIKE '%bakery%'; -- all witnesses mentioned 'bakery'

-- One witness (Ruth) saw the thief drive away from the bakery parking lot 10 minutes after theft so the bakery security logs are checked
-- Getting the license plate of suspects that left the bakery around a time frame 10 mins after theft
SELECT license_plate FROM bakery_security_logs WHERE year=2021 AND month=7 AND day=28 AND hour=10 AND minute BETWEEN 15 AND 35 AND activity = 'exit';
