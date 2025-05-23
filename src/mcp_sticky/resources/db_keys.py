#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-19 12:46:24 Monday

@author: Nikhil Kapila
"""

# Templates dictionary converted from pickle

templates = {   
    'buzz': 'buzz',
    '10 Guy': 'tenguy',
    'Afraid to Ask Andy': 'afraid',
    'Agnes Harkness Winking': 'agnes',
    'All Your Base Are Belong to Us': 'zero-wing',
    'Almost Politically Correct Redneck': 'apcr',
    'Always Has Been': 'astronaut',
    'American Chopper Argument': 'chair',
    'An Older Code Sir, But It Checks Out': 'older',
    'Anakin and Padme Change the World For the Better': 'right',
    'Ancient Aliens Guy': 'aag',
    "And It's Gone": 'gone',
    'And Then I Said': 'atis',
    'Are You Two Friends?': 'friends',
    'At Least You Tried': 'tried',
    'Awkward Moment Seal': 'ams',
    'Baby Insanity Wolf': 'biw',
    "Baby, You've Got a Stew Going": 'stew',
    'Bad Luck Brian': 'blb',
    'Bongo Cat': 'bongo',
    "But It's Honest Work": 'bihw',
    "But That's None of My Business": 'kermit',
    'Butthurt Dweller': 'bd',
    'Captain America Elevator Fight Dad Joke': 'captain-america',
    'Captain Hindsight': 'ch',
    'Change My Mind': 'cmm',
    'Cheems': 'cheems',
    'Comic Book Guy': 'cbg',
    'Communist Bugs Bunny': 'cbb',
    'Condescending Wonka': 'wonka',
    'Confession Bear': 'cb',
    'Confused Gandalf': 'gandalf',
    'Conspiracy Keanu': 'keanu',
    'Crying on Floor': 'cryingfloor',
    'Daily Struggle': 'ds',
    'Dating Site Murderer': 'dsm',
    'Disaster Girl': 'disastergirl',
    'Distracted Boyfriend': 'db',
    'Distracted Girlfriend': 'dg',
    'Do It Live!': 'live',
    'Do You Want Ants?': 'ants',
    'Doge': 'doge',
    'Donald Trump': 'trump',
    'Drakeposting': 'drake',
    'Drowning High Five': 'drowning',
    'Drunk Baby': 'drunk',
    'Elmo Choosing Cocaine': 'elmo',
    'Ermahgerd': 'ermg',
    'Everything the Light Touches is Our Kingdom': 'light',
    'Expectation vs. Reality': 'dbg',
    'Facepalm': 'facepalm',
    'Fake Spirit Halloween Costume': 'spirit',
    'Feels Bad Man': 'sadfrog',
    'Feels Good': 'feelsgood',
    'First Try!': 'firsttry',
    'First World Problems': 'fwp',
    'Forever Alone': 'fa',
    'Foul Bachelor Frog': 'fbf',
    'Fuck Me, Right?': 'fmr',
    'Futurama Fry': 'fry',
    'Galaxy Brain': 'gb',
    'Genie Lamp': 'genie',
    'Genie Rules': 'wishes',
    'Get Better Material': 'crow',
    'Good Guy Greg': 'ggg',
    "Grant Gustin Next To Oliver Queen's Grave": 'grave',
    "Gru's Plan": 'gru',
    'Grumpy Cat': 'grumpycat',
    'Guy Hammering Nails Into Sand': 'nails',
    'Hide the Pain Harold': 'harold',
    'Hipster Barista': 'hipster',
    'I Can Has Cheezburger?': 'icanhas',
    "I Feel Like I'm Taking Crazy Pills": 'crazypills',
    'I Guarantee It': 'mw',
    "I Have No Idea What I'm Doing": 'noidea',
    'I Immediately Regret This Decision!': 'regret',
    'I Made This': 'made',
    'I Should Buy a Boat Cat': 'boat',
    'I Should Not Have Said That': 'hagrid',
    'I Would Be So Happy': 'sohappy',
    'I am the Captain Now': 'captain',
    "I'm Going to Build My Own Theme Park": 'bender',
    'Inhaling Seagull': 'seagull',
    'Inigo Montoya': 'inigo',
    'Insanity Wolf': 'iw',
    'Is This a Pigeon?': 'pigeon',
    "It's A Trap!": 'ackbar',
    "It's Happening": 'happening',
    "It's Simple, Kill the Batman": 'joker',
    'Jim Halpert Pointing to Whiteboard': 'jim',
    'Jony Ive Redesigns Things': 'ive',
    'Joseph Ducreux': 'jd',
    'Karate Kyle': 'kk',
    'Khaby Lame Shrug': 'khaby-lame',
    'Kombucha Girl': 'kombucha',
    "Kramer, What's Going On In There?": 'kramer',
    'Laughing Lizard': 'll',
    'Laundry Room Viking': 'lrv',
    'Left Exit 12 Off Ramp': 'exit',
    'Leo Strutting': 'leo',
    'Life... Finds a Way': 'away',
    'Matrix Morpheus': 'morpheus',
    'Member Berries': 'mb',
    'Men in Black': 'because',
    'Michael Scott No God No': 'michael-scott',
    'Midwit': 'midwit',
    'Milk Was a Bad Choice': 'badchoice',
    'Mini Keanu Reeves': 'mini-keanu',
    'Minor Mistake Marvin': 'mmm',
    'Mocking Spongebob': 'spongebob',
    'Mother Ignoring Kid Drowning In A Pool': 'pool',
    'No Soup for You': 'soup-nazi',
    'No Take, Only Throw': 'ntot',
    'Nothing To Do Here': 'jetpack',
    'Office Space Milton': 'cake',
    "Oh, I'm Sorry, I Thought This Was America": 'imsorry',
    "Oh, Is That What We're Going to Do Today?": 'red',
    'One Does Not Simply Walk into Mordor': 'mordor',
    'Oprah You Get a Car': 'oprah',
    'Overly Attached Girlfriend': 'oag',
    'Panik Kalm Panik': 'panik-kalm-panik',
    "Patrick Star's Wallet": 'wallet',
    'Pepperidge Farm Remembers': 'remembers',
    'Perfection': 'perfection',
    'Persian Cat Room Guardian': 'persian',
    "Peter Parker's Glasses": 'glasses',
    'Philosoraptor': 'philosoraptor',
    'Phoebe Teaching Joey': 'ptj',
    'Principal Skinner': 'touch',
    'Probably Not a Good Idea': 'jw',
    'Push it somewhere else Patrick': 'patrick',
    'Roll Safe': 'rollsafe',
    'Running Away Balloon': 'balloon',
    'Sad Barack Obama': 'sad-obama',
    'Sad Bill Clinton': 'sad-clinton',
    'Sad George Bush': 'sad-bush',
    'Sad Joe Biden': 'sad-biden',
    'Sad John Boehner': 'sad-boehner',
    'Salt Bae': 'saltbae',
    'Sarcastic Bear': 'sarcasticbear',
    'Say the Line, Bart!': 'say',
    'Schrute Facts': 'dwight',
    'Scooby Doo Reveal': 'reveal',
    'Scumbag Brain': 'sb',
    'Scumbag Steve': 'ss',
    'Seal of Approval': 'soa',
    'Sealed Fate': 'sf',
    'See? Nobody Cares': 'dodgson',
    'Shut Up and Take My Money!': 'money',
    'Skeptical Snake': 'snek',
    'Skeptical Third World Kid': 'sk',
    'So Hot Right Now': 'sohot',
    "So I Got That Goin' For Me, Which is Nice": 'nice',
    'Socially Awesome Awkward Penguin': 'awesome-awkward',
    'Socially Awesome Penguin': 'awesome',
    'Socially Awkward Awesome Penguin': 'awkward-awesome',
    'Socially Awkward Penguin': 'awkward',
    'Spider-Man Pointing at Spider-Man': 'spiderman',
    'Stonks': 'stonks',
    "Stop It Patrick You're Scaring Him": 'stop',
    'Stop It, Get Some Help': 'stop-it',
    'Stop Trying to Make Fetch Happen': 'fetch',
    'Success Kid': 'success',
    'Sudden Clarity Clarence': 'scc',
    'Super Cool Ski Instructor': 'ski',
    'Sweet Brown': 'aint-got-time',
    'That Would Be Great': 'officespace',
    'The Most Interesting Man in the World': 'interesting',
    'The Rent Is Too Damn High': 'toohigh',
    'The Worst Day Of Your Life So Far': 'worst',
    "They're The Same Picture": 'same',
    'This is Bull, Shark': 'bs',
    'This is Fine': 'fine',
    'This is Sparta!': 'sparta',
    'Too Confusing, Too Extreme': 'prop3',
    'Tuxedo Winnie the Pooh': 'pooh',
    'Two Guys on a Bus': 'bus',
    'Types of Headaches': 'headaches',
    'Ugandan Knuckles': 'ugandanknuck',
    'Unpopular opinion puffin': 'puffin',
    'Vince McMahon Reaction': 'vince',
    "We Don't Do That Here": 'wddth',
    'We Have Food at Home': 'home',
    'What Are Ya Gonna Do?': 'waygd',
    'What Color Do You Want Your Dragon': 'dragon',
    'What Year Is It?': 'whatyear',
    'What a Country': 'country',
    'What is this, a Center for Ants?!': 'center',
    'What the Hell is This?': 'noah',
    "What's in the box!?": 'box',
    'Who Killed Hannibal?': 'wkh',
    'Why Not Both?': 'both',
    "Why Shouldn't I Keep It": 'bilbo',
    'Will Smith Slapping Chris Rock': 'slap',
    'Winter is coming': 'winter',
    "Woman Holding Dog's Mouth": 'mouth',
    'Woman Yelling at a Cat': 'woman-cat',
    'X all the Y': 'xy',
    'Xzibit Yo Dawg': 'yodawg',
    'Y U NO Guy': 'yuno',
    "Y'all Got Any More of Them": 'yallgot',
    'You Guys Are Getting Paid?': 'millers',
    'You Know What Really Grinds My Gears?': 'gears',
    'You Should Feel Bad': 'bad',
    'You Sit on a Throne of Lies': 'elf',
    'You Were the Chosen One!': 'chosen'
    }
