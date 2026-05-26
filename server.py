from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector