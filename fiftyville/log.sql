-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Getting the description of the crime from crime scene reports data
SELECT description FROM crime_scene_reports WHERE year=2021 AND month=7 AND day=28 AND street = "Humphrey Street";

-- Since description mentions that interviews where conducted on three witnesses, we are going to check the interview data for more information
-- Get names and transcripts of the witnesses
SELECT name, transcript FROM interviews WHERE month=7 AND day=28 AND year=2021 AND transcript LIKE '%bakery%'; -- all witnesses mentioned 'bakery'

-- check passengers of earliest flight out of fiftyville on July 29;
SELECT id, destination_airport_id, hour, minute FROM flights WHERE origin_airport_id = (SELECT id FROM airports WHERE city= 'Fiftyville') AND year=2021 AND month=7 AND day=29;
-- From the data above I selected the earliest flight (8:20), with flight id of 36 and destination airport id of 4

-- Check the bakery security logs to get the license plate of suspects that left the bakery around a time frame 10 mins after theft;
-- atm transactions to get account numbers from which money was withdrawn at an atm on Leggett Street in the morning of the same day;
-- bank accounts to get suspects' person ids from the account numbers obtained;
-- phone calls to check callers at the day and time of crime with call duration of less than a minute;
--then identify suspects that matched the data
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year=2021 AND month=7 AND day=28 AND atm_location= "Leggett Street" AND transaction_type= 'withdraw')) AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year=2021 AND month=7 AND day=28 AND hour=10 AND minute BETWEEN 15 AND 35 AND activity = 'exit') AND phone_number IN (SELECT caller FROM phone_calls WHERE year=2021 AND month=7 AND day=28 AND duration<60) AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id=36);


-- The city the thief escaped to found from the destination airport id and airports table
SELECT city FROM airports WHERE id = 4;

-- The accomplice is the receiver of the call from the thief on the day and time of theft
SELECT name FROM people WHERE phone_number= (SELECT receiver FROM phonecalls WHERE )