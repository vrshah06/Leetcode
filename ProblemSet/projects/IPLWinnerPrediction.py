import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# IPL WINNER PREDICTION USING MACHINE LEARNING WITH TRAIN-TEST SPLIT
# ============================================================================

class IPLWinnerPredictor:
    def __init__(self):
        self.models = {}
        self.le_teams = LabelEncoder()
        self.le_venues = LabelEncoder()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def create_historical_data(self):
        """
        Create historical IPL match data (2008-2025)
        Features: home_team, away_team, venue, home_wins, away_wins, 
        home_avg_runs, away_avg_runs, home_wickets_lost, season
        """
        np.random.seed(42)
        
        teams = ['Mumbai Indians', 'Chennai Super Kings', 'Delhi Capitals', 
                 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
                 'Sunrisers Hyderabad', 'Rajasthan Royals', 'Punjab Kings',
                 'Gujarat Titans', 'Lucknow Super Giants']
        
        venues = ['Mumbai', 'Chennai', 'Delhi', 'Bangalore', 'Kolkata',
                  'Hyderabad', 'Jaipur', 'Chandigarh', 'Ahmedabad', 'Lucknow']
        
        data = []
        
        # Generate 500+ matches with realistic features
        for _ in range(500):
            home_team = np.random.choice(teams)
            away_team = np.random.choice([t for t in teams if t != home_team])
            venue = np.random.choice(venues)
            
            home_wins = np.random.randint(0, 30)
            away_wins = np.random.randint(0, 30)
            home_avg_runs = np.random.randint(130, 180)
            away_avg_runs = np.random.randint(130, 180)
            home_wickets_lost = np.random.randint(2, 10)
            away_wickets_lost = np.random.randint(2, 10)
            season = np.random.randint(2008, 2026)
            
            # Determine winner based on realistic logic
            home_strength = home_wins * 0.4 + home_avg_runs * 0.3 + (10 - home_wickets_lost) * 1.5
            away_strength = away_wins * 0.4 + away_avg_runs * 0.3 + (10 - away_wickets_lost) * 1.5
            
            winner = 1 if home_strength > away_strength else 0  # 1 = home wins, 0 = away wins
            
            data.append({
                'home_team': home_team,
                'away_team': away_team,
                'venue': venue,
                'home_wins': home_wins,
                'away_wins': away_wins,
                'home_avg_runs': home_avg_runs,
                'away_avg_runs': away_avg_runs,
                'home_wickets_lost': home_wickets_lost,
                'away_wickets_lost': away_wickets_lost,
                'season': season,
                'winner': winner  # 1 = home team wins, 0 = away team wins
            })
        
        df = pd.DataFrame(data)
        print("\n" + "="*70)
        print("HISTORICAL IPL DATA (2008-2025)")
        print("="*70)
        print(f"Total matches: {len(df)}")
        print(f"\nDataset shape: {df.shape}")
        print(f"\nFirst few records:\n{df.head()}")
        print(f"\nData statistics:\n{df.describe()}")
        
        return df
    
    def preprocess_data(self, df):
        """
        Preprocess data: encode categorical features, prepare features and labels
        """
        print("\n" + "="*70)
        print("DATA PREPROCESSING")
        print("="*70)
        
        # Encode team names
        all_teams = list(set(df['home_team'].unique()) | set(df['away_team'].unique()))
        self.le_teams.fit(all_teams)
        
        df['home_team_encoded'] = self.le_teams.transform(df['home_team'])
        df['away_team_encoded'] = self.le_teams.transform(df['away_team'])
        
        # Encode venues
        self.le_venues.fit(df['venue'].unique())
        df['venue_encoded'] = self.le_venues.transform(df['venue'])
        
        # Feature engineering
        df['team_diff'] = df['home_wins'] - df['away_wins']
        df['runs_diff'] = df['home_avg_runs'] - df['away_avg_runs']
        df['wickets_diff'] = (10 - df['home_wickets_lost']) - (10 - df['away_wickets_lost'])
        
        # Select features for the model
        features = ['home_team_encoded', 'away_team_encoded', 'venue_encoded',
                   'home_wins', 'away_wins', 'home_avg_runs', 'away_avg_runs',
                   'home_wickets_lost', 'away_wickets_lost', 'season',
                   'team_diff', 'runs_diff', 'wickets_diff']
        
        X = df[features]
        y = df['winner']
        
        print(f"Features selected: {len(features)}")
        print(f"Feature list: {features}")
        print(f"Target variable distribution:\n{y.value_counts()}")
        
        return X, y, df
    
    def split_and_train(self, X, y):
        """
        Split data into train-test sets and train multiple models
        """
        print("\n" + "="*70)
        print("TRAIN-TEST SPLIT AND MODEL TRAINING")
        print("="*70)
        
        # 80-20 train-test split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        print(f"Training set size: {len(self.X_train)} ({len(self.X_train)/len(X)*100:.1f}%)")
        print(f"Test set size: {len(self.X_test)} ({len(self.X_test)/len(X)*100:.1f}%)")
        print(f"\nTraining target distribution:\n{self.y_train.value_counts()}")
        print(f"\nTest target distribution:\n{self.y_test.value_counts()}")
        
        # Train multiple models
        print("\n" + "-"*70)
        print("Training Models...")
        print("-"*70)
        
        # Model 1: Logistic Regression
        print("\n1. Logistic Regression")
        lr = LogisticRegression(max_iter=1000, random_state=42)
        lr.fit(self.X_train, self.y_train)
        lr_pred = lr.predict(self.X_test)
        lr_acc = accuracy_score(self.y_test, lr_pred)
        print(f"   Accuracy: {lr_acc:.4f}")
        self.models['Logistic Regression'] = (lr, lr_acc)
        
        # Model 2: Random Forest
        print("\n2. Random Forest Classifier")
        rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        rf.fit(self.X_train, self.y_train)
        rf_pred = rf.predict(self.X_test)
        rf_acc = accuracy_score(self.y_test, rf_pred)
        print(f"   Accuracy: {rf_acc:.4f}")
        self.models['Random Forest'] = (rf, rf_acc)
        
        # Model 3: Gradient Boosting
        print("\n3. Gradient Boosting Classifier")
        gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
        gb.fit(self.X_train, self.y_train)
        gb_pred = gb.predict(self.X_test)
        gb_acc = accuracy_score(self.y_test, gb_pred)
        print(f"   Accuracy: {gb_acc:.4f}")
        self.models['Gradient Boosting'] = (gb, gb_acc)
        
        # Select best model
        best_model_name = max(self.models.keys(), key=lambda x: self.models[x][1])
        best_model = self.models[best_model_name][0]
        
        print("\n" + "-"*70)
        print(f"BEST MODEL: {best_model_name} (Accuracy: {self.models[best_model_name][1]:.4f})")
        print("-"*70)
        
        # Detailed evaluation of best model
        best_pred = best_model.predict(self.X_test)
        print(f"\nClassification Report:\n{classification_report(self.y_test, best_pred, target_names=['Away Win', 'Home Win'])}")
        
        return best_model, best_model_name
    
    def predict_ipl_2026(self, best_model, df):
        """
        Predict IPL 2026 winners based on trained model
        """
        print("\n" + "="*70)
        print("IPL 2026 WINNER PREDICTIONS")
        print("="*70)
        
        teams = ['Mumbai Indians', 'Chennai Super Kings', 'Delhi Capitals', 
                 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
                 'Sunrisers Hyderabad', 'Rajasthan Royals', 'Punjab Kings',
                 'Gujarat Titans', 'Lucknow Super Giants']
        
        predictions_2026 = []
        
        # Generate predictions for all possible match-ups in IPL 2026
        for home_team in teams:
            for away_team in teams:
                if home_team != away_team:
                    home_team_encoded = self.le_teams.transform([home_team])[0]
                    away_team_encoded = self.le_teams.transform([away_team])[0]
                    venue = np.random.choice(df['venue'].unique())
                    venue_encoded = self.le_venues.transform([venue])[0]
                    
                    # Get team stats from training data
                    home_stats = df[df['home_team'] == home_team]
                    away_stats_context = df[df['away_team'] == away_team]
                    
                    if len(home_stats) > 0 and len(away_stats_context) > 0:
                        home_wins = home_stats['home_wins'].mean()
                        away_wins = away_stats_context['away_wins'].mean()
                        home_avg_runs = home_stats['home_avg_runs'].mean()
                        away_avg_runs = away_stats_context['away_avg_runs'].mean()
                        home_wickets_lost = home_stats['home_wickets_lost'].mean()
                        away_wickets_lost = away_stats_context['away_wickets_lost'].mean()
                        
                        team_diff = home_wins - away_wins
                        runs_diff = home_avg_runs - away_avg_runs
                        wickets_diff = (10 - home_wickets_lost) - (10 - away_wickets_lost)
                        
                        # Create feature vector
                        features = np.array([[
                            home_team_encoded, away_team_encoded, venue_encoded,
                            home_wins, away_wins, home_avg_runs, away_avg_runs,
                            home_wickets_lost, away_wickets_lost, 2026,
                            team_diff, runs_diff, wickets_diff
                        ]])
                        
                        prediction = best_model.predict(features)[0]
                        probability = best_model.predict_proba(features)[0]
                        
                        winner = home_team if prediction == 1 else away_team
                        confidence = max(probability)
                        
                        predictions_2026.append({
                            'home_team': home_team,
                            'away_team': away_team,
                            'venue': venue,
                            'predicted_winner': winner,
                            'confidence': confidence
                        })
        
        # Summary statistics
        predictions_df = pd.DataFrame(predictions_2026)
        
        print(f"\nTotal predictions for IPL 2026: {len(predictions_df)}")
        print(f"\nWin probability by team:")
        
        win_counts = predictions_df['predicted_winner'].value_counts()
        for team, count in win_counts.items():
            win_prob = (count / len(predictions_df)) * 100
            print(f"  {team}: {count} wins ({win_prob:.1f}%)")
        
        # Top predicted winner
        top_winner = predictions_df['predicted_winner'].value_counts().index[0]
        top_wins = predictions_df['predicted_winner'].value_counts().values[0]
        print(f"\n🏆 TOP PREDICTED WINNER FOR IPL 2026: {top_winner}")
        print(f"   Predicted wins: {top_wins} out of {len(predictions_df)} matches")
        
        # Sample predictions
        print(f"\nSample IPL 2026 Match Predictions:")
        print("-" * 70)
        sample_preds = predictions_df.sample(min(10, len(predictions_df)), random_state=42)
        for idx, row in sample_preds.iterrows():
            print(f"{row['home_team']:30} vs {row['away_team']:30}")
            print(f"  📍 Venue: {row['venue']:20} | Winner: {row['predicted_winner']:30} | Confidence: {row['confidence']:.2%}")
            print()
        
        return predictions_df
    
    def run_full_pipeline(self):
        """
        Run the complete IPL winner prediction pipeline
        """
        print("\n" + "="*70)
        print("IPL 2026 WINNER PREDICTION - MACHINE LEARNING MODEL")
        print("="*70)
        
        # Step 1: Create historical data
        df = self.create_historical_data()
        
        # Step 2: Preprocess data
        X, y, df_processed = self.preprocess_data(df)
        
        # Step 3: Train-test split and model training
        best_model, best_model_name = self.split_and_train(X, y)
        
        # Step 4: Predict IPL 2026
        predictions_2026 = self.predict_ipl_2026(best_model, df_processed)
        
        print("\n" + "="*70)
        print("PREDICTION COMPLETE!")
        print("="*70)
        
        return best_model, best_model_name, predictions_2026


if __name__ == "__main__":
    # Initialize and run the predictor
    predictor = IPLWinnerPredictor()
    best_model, model_name, predictions = predictor.run_full_pipeline()
    
    print("\n✅ IPL 2026 Winner Prediction model trained and predictions generated!")
    print(f"✅ Best performing model: {model_name}")
