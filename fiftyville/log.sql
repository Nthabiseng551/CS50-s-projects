-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Getting the description of the crime from crime scene reports data
SELECT description FROM crime_scene_reports WHERE year=2021 AND month=7 AND day=28 AND street = "Humphrey Street";

-- Since description mentions that interviews where conducted on three witnesses, we are going to check the interview data for more information
-- Get names and transcripts of the witnesses
SELECT name, transcript FROM interviews WHERE month=7 AND day=28 AND year=2021 AND transcript LIKE '%bakery%'; -- all witnesses mentioned 'bakery'

-- Check the bakery security logs to get the license plate of suspects that left the bakery around a time frame 10 mins after theft;
-- atm transactions to get account numbers from which money was withdrawn at an atm on Leggett Street in the morning of the same day;
-- bank accounts to get suspects' person ids from the account numbers obtained; then identify suspects that matched the data
SELECT name, phonenumber, passportnumber FROM people WHERE id IN (SELECT personid FROM bankaccounts WHERE accountnumber IN (SELECT accountnumber FROM atmtransactions WHERE year2021 AND month7 AND day28 AND atmlocation "Leggett Street" AND transactiontype 'withdraw')) AND licenseplate IN (SELECT license_plate FROM bakery_security_logs WHERE year=2021 AND month=7 AND day=28 AND hour=10 AND minute BETWEEN 15 AND 35 AND activity = 'exit');
