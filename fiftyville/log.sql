-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Getting the description of the crime from crime scene reports table
SELECT description FROM crime_scene_reports WHERE year=2021 AND month=7 AND day=28 AND street = "Humphrey Street";

-- since description mentions that interviews where conducted on three witnesses, we are going to check the inter