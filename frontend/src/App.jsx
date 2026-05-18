import React, { useState, useEffect } from 'react';
import './index.css';

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

const LOCALITIES = [
  "Banashankari",
  "Banaswadi",
  "Bannerghatta Road",
  "Basavanagudi",
  "Basaveshwara Nagar",
  "Bellandur",
  "Bommanahalli",
  "Brigade Road",
  "Brookefield",
  "BTM Layout",
  "Church Street",
  "Commercial Street",
  "Cunningham Road",
  "CV Raman Nagar",
  "Domlur",
  "Electronic City",
  "Frazer Town",
  "HSR Layout",
  "Indiranagar",
  "Infantry Road",
  "Jayanagar",
  "Jeevan Bhima Nagar",
  "JP Nagar",
  "Kalyan Nagar",
  "Kammanahalli",
  "Koramangala",
  "Lavelle Road",
  "Majestic",
  "Malleshwaram",
  "Marathahalli",
  "MG Road",
  "New Bel Road",
  "Old Airport Road",
  "Rajajinagar",
  "Residency Road",
  "Richmond Road",
  "Sadashiv Nagar",
  "Sarjapur Road",
  "Seshadripuram",
  "Shanti Nagar",
  "Shivajinagar",
  "St. Marks Road",
  "Ulsoor",
  "Whitefield"
];

const CUISINES = [
  "Afghan",
  "Afghani",
  "African",
  "American",
  "Andhra",
  "Arabian",
  "Asian",
  "Assamese",
  "Australian",
  "Awadhi",
  "BBQ",
  "Bakery",
  "Bar Food",
  "Belgian",
  "Bengali",
  "Beverages",
  "Bihari",
  "Biryani",
  "Bohri",
  "British",
  "Bubble Tea",
  "Burger",
  "Burmese",
  "Cafe",
  "Cantonese",
  "Charcoal Chicken",
  "Chettinad",
  "Chinese",
  "Coffee",
  "Continental",
  "Desserts",
  "Drinks Only",
  "European",
  "Fast Food",
  "Finger Food",
  "French",
  "German",
  "Goan",
  "Greek",
  "Grill",
  "Gujarati",
  "Healthy Food",
  "Hot dogs",
  "Hyderabadi",
  "Ice Cream",
  "Indian",
  "Indonesian",
  "Iranian",
  "Italian",
  "Japanese",
  "Jewish",
  "Juices",
  "Kashmiri",
  "Kebab",
  "Kerala",
  "Konkan",
  "Korean",
  "Lebanese",
  "Lucknowi",
  "Maharashtrian",
  "Malaysian",
  "Malwani",
  "Mangalorean",
  "Mediterranean",
  "Mexican",
  "Middle Eastern",
  "Mithai",
  "Modern Indian",
  "Momos",
  "Mongolian",
  "Mughlai",
  "Naga",
  "Nepalese",
  "North Eastern",
  "North Indian",
  "Oriya",
  "Paan",
  "Pan Asian",
  "Parsi",
  "Pizza",
  "Portuguese",
  "Rajasthani",
  "Raw Meats",
  "Roast Chicken",
  "Rolls",
  "Russian",
  "Salad",
  "Sandwich",
  "Seafood",
  "Sindhi",
  "Singaporean",
  "South American",
  "South Indian",
  "Spanish",
  "Sri Lankan",
  "Steak",
  "Street Food",
  "Sushi",
  "Tamil",
  "Tea",
  "Tex-Mex",
  "Thai",
  "Tibetan",
  "Turkish",
  "Vegan",
  "Vietnamese",
  "Wraps"
];


function App() {
  const [prefs, setPrefs] = useState({
    city: '',
    budget: 'Low',
    cuisines: '',
    min_rating: 0.0,
    additional_context: ''
  });
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const [cuisineSearch, setCuisineSearch] = useState('');
  const [selectedCuisines, setSelectedCuisines] = useState([]);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  useEffect(() => {
    const handleOutsideClick = (e) => {
      if (!e.target.closest('#cuisine-search-container')) {
        setDropdownOpen(false);
      }
    };
    window.addEventListener('click', handleOutsideClick);
    return () => window.removeEventListener('click', handleOutsideClick);
  }, []);

  const handleAddCuisine = (cuisine) => {
    if (selectedCuisines.length >= 2) return;
    if (!selectedCuisines.includes(cuisine)) {
      const updated = [...selectedCuisines, cuisine];
      setSelectedCuisines(updated);
      setPrefs(prev => ({ ...prev, cuisines: updated.join(', ') }));
    }
    setCuisineSearch('');
    setDropdownOpen(false);
  };

  const handleRemoveCuisine = (cuisine) => {
    const updated = selectedCuisines.filter(c => c !== cuisine);
    setSelectedCuisines(updated);
    setPrefs(prev => ({ ...prev, cuisines: updated.join(', ') }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResults(null);

    try {
      const response = await fetch(`${API_BASE}/api/v1/recommend?count=5`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...prefs,
          cuisines: prefs.cuisines ? prefs.cuisines.split(',').map(c => c.trim()) : []
        })
      });

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.detail || 'Failed to fetch recommendations');
      }

      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container" style={{ 
      maxWidth: '800px', 
      margin: '0 auto', 
      padding: '40px 20px',
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: results || loading || error ? 'flex-start' : 'center',
      transition: 'all 0.5s cubic-bezier(0.4, 0, 0.2, 1)'
    }}>
      <header className="fade-in" style={{ textAlign: 'center', marginBottom: '30px' }}>
        <h1 style={{ fontSize: '3rem', fontWeight: 800, marginBottom: '5px', background: 'linear-gradient(to right, #fff, #ff4d4d)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
          Zomato AI
        </h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '1rem' }}>Personalized Bangalore Restaurant Recommendations</p>
      </header>

      <main style={{ 
        width: '100%', 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center', 
        gap: '40px' 
      }}>
        {/* Sidebar Form */}
        <section className="glass-card fade-in" style={{ 
          padding: '30px', 
          width: '100%', 
          maxWidth: '600px',
          boxShadow: '0 8px 32px 0 rgba(255, 77, 77, 0.12)'
        }}>
          <h2 style={{ marginBottom: '24px', fontSize: '1.5rem' }}>Your Preferences</h2>
          <form onSubmit={handleSubmit}>
            <div style={{ marginBottom: '20px' }}>
              <label style={{ display: 'block', marginBottom: '8px', color: 'var(--text-muted)', fontSize: '0.9rem' }}>City / Locality</label>
              <select 
                className="form-input" 
                value={prefs.city} 
                onChange={e => setPrefs({...prefs, city: e.target.value})}
                style={{
                  background: 'rgba(255, 255, 255, 0.03)',
                  border: '1px solid var(--glass-border)',
                  borderRadius: '12px',
                  padding: '12px 16px',
                  color: 'white',
                  width: '100%',
                  outline: 'none',
                  cursor: 'pointer'
                }}
              >
                <option value="" style={{ background: 'var(--bg-dark)', color: 'var(--text-muted)' }}>All Localities (Bangalore)</option>
                {LOCALITIES.map(loc => (
                  <option key={loc} value={loc} style={{ background: 'var(--bg-dark)', color: 'white' }}>
                    {loc}
                  </option>
                ))}
              </select>
            </div>

            <div style={{ marginBottom: '20px' }}>
              <label style={{ display: 'block', marginBottom: '8px', color: 'var(--text-muted)', fontSize: '0.9rem' }}>Budget Band</label>
              <div style={{ display: 'flex', gap: '10px' }}>
                {['Low', 'Medium', 'High'].map(b => (
                  <button
                    key={b}
                    type="button"
                    onClick={() => setPrefs({...prefs, budget: b})}
                    style={{
                      flex: 1,
                      padding: '8px',
                      borderRadius: '8px',
                      border: '1px solid var(--glass-border)',
                      background: prefs.budget === b ? 'var(--primary)' : 'transparent',
                      color: 'white',
                      cursor: 'pointer',
                      fontSize: '0.8rem'
                    }}
                  >
                    {b}
                  </button>
                ))}
              </div>
            </div>

            <div id="cuisine-search-container" style={{ marginBottom: '20px', position: 'relative' }}>
              <label style={{ display: 'block', marginBottom: '8px', color: 'var(--text-muted)', fontSize: '0.9rem' }}>Cuisines</label>
              
              <div 
                style={{
                  background: 'rgba(255, 255, 255, 0.03)',
                  border: '1px solid var(--glass-border)',
                  borderRadius: '12px',
                  padding: '8px 12px',
                  display: 'flex',
                  flexWrap: 'wrap',
                  gap: '6px',
                  alignItems: 'center',
                  minHeight: '48px',
                  cursor: 'text',
                  transition: 'border-color 0.3s'
                }}
                onClick={() => document.getElementById('cuisine-search-input')?.focus()}
              >
                {selectedCuisines.map(c => (
                  <span 
                    key={c} 
                    style={{
                      background: 'rgba(255, 77, 77, 0.15)',
                      border: '1px solid rgba(255, 77, 77, 0.3)',
                      borderRadius: '6px',
                      padding: '3px 8px',
                      fontSize: '0.8rem',
                      color: 'white',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '6px'
                    }}
                  >
                    {c}
                    <span 
                      style={{ cursor: 'pointer', fontWeight: 'bold', color: 'var(--primary)', padding: '0 2px' }}
                      onClick={(e) => {
                        e.stopPropagation();
                        handleRemoveCuisine(c);
                      }}
                    >
                      ×
                    </span>
                  </span>
                ))}
                
                <input
                  id="cuisine-search-input"
                  type="text"
                  value={cuisineSearch}
                  onChange={e => {
                    setCuisineSearch(e.target.value);
                    setDropdownOpen(true);
                  }}
                  onFocus={() => {
                    if (selectedCuisines.length < 2) {
                      setDropdownOpen(true);
                    }
                  }}
                  placeholder={
                    selectedCuisines.length >= 2 
                      ? "Max 2 selected" 
                      : selectedCuisines.length > 0 
                        ? "" 
                        : "Search & add cuisines... (Default: All)"
                  }
                  readOnly={selectedCuisines.length >= 2}
                  style={{
                    background: 'transparent',
                    border: 'none',
                    outline: 'none',
                    color: 'white',
                    fontSize: '0.9rem',
                    flex: '1',
                    minWidth: '150px',
                    cursor: selectedCuisines.length >= 2 ? 'not-allowed' : 'text'
                  }}
                />
              </div>

              {dropdownOpen && selectedCuisines.length < 2 && (
                <div 
                  style={{
                    position: 'absolute',
                    top: '100%',
                    left: 0,
                    right: 0,
                    marginTop: '8px',
                    background: 'var(--bg-dark)',
                    border: '1px solid var(--glass-border)',
                    borderRadius: '12px',
                    maxHeight: '200px',
                    overflowY: 'auto',
                    zIndex: 1000,
                    boxShadow: '0 10px 30px rgba(0,0,0,0.5)'
                  }}
                >
                  {CUISINES.filter(c => 
                    c.toLowerCase().includes(cuisineSearch.toLowerCase()) && 
                    !selectedCuisines.includes(c)
                  ).length === 0 ? (
                    <div style={{ padding: '12px 16px', color: 'var(--text-muted)', fontSize: '0.9rem' }}>
                      No matching cuisines found
                    </div>
                  ) : (
                    CUISINES.filter(c => 
                      c.toLowerCase().includes(cuisineSearch.toLowerCase()) && 
                      !selectedCuisines.includes(c)
                    ).map(c => (
                      <div 
                        key={c}
                        onClick={() => handleAddCuisine(c)}
                        style={{
                          padding: '10px 16px',
                          color: 'white',
                          cursor: 'pointer',
                          fontSize: '0.9rem',
                          transition: 'background 0.2s',
                          borderBottom: '1px solid rgba(255,255,255,0.02)'
                        }}
                        onMouseEnter={e => e.target.style.background = 'rgba(255, 77, 77, 0.1)'}
                        onMouseLeave={e => e.target.style.background = 'transparent'}
                      >
                        {c}
                      </div>
                    ))
                  )}
                </div>
              )}
            </div>

            <div style={{ marginBottom: '20px' }}>
              <label style={{ display: 'block', marginBottom: '8px', color: 'var(--text-muted)', fontSize: '0.9rem', fontWeight: 'bold' }}>Min Rating: {prefs.min_rating}</label>
              <input 
                type="range" min="0" max="5" step="0.1"
                style={{ width: '100%', accentColor: 'var(--primary)' }}
                value={prefs.min_rating} 
                onChange={e => setPrefs({...prefs, min_rating: parseFloat(e.target.value)})}
              />
            </div>

            <div style={{ marginBottom: '30px' }}>
              <label style={{ display: 'block', marginBottom: '8px', color: 'var(--text-muted)', fontSize: '0.9rem' }}>Additional Context</label>
              <textarea 
                className="form-input" 
                rows="3"
                value={prefs.additional_context} 
                onChange={e => setPrefs({...prefs, additional_context: e.target.value})}
                placeholder="e.g. Family friendly, outdoor seating..."
              />
            </div>

            <button type="submit" className="btn-primary" style={{ width: '100%' }} disabled={loading}>
              {loading ? 'Finding Best Spots...' : 'Get Recommendations'}
            </button>
          </form>
        </section>

        {/* Results Area */}
        <section style={{ width: '100%', maxWidth: '600px' }}>
          {loading && (
            <div className="fade-in" style={{ textAlign: 'center', padding: '100px 0' }}>
              <div className="spinner" style={{ width: '50px', height: '50px', border: '4px solid var(--glass)', borderTopColor: 'var(--primary)', borderRadius: '50%', animation: 'spin 1s linear infinite', margin: '0 auto 20px' }}></div>
              <p style={{ color: 'var(--text-muted)', fontSize: '1.1rem' }}>Our AI is analyzing the best restaurants for you...</p>
            </div>
          )}

          {error && (
            <div className="glass-card fade-in" style={{ padding: '30px', borderLeft: '4px solid #ff4d4d' }}>
              <h3 style={{ color: '#ff4d4d', marginBottom: '10px' }}>Oops!</h3>
              <p style={{ color: 'var(--text-muted)' }}>{error}</p>
            </div>
          )}

          {results && (
            <div className="fade-in">

               {results.recommendations.map((rec, i) => (
                <div key={i} className="glass-card" style={{ padding: '30px', marginBottom: '24px', transition: 'transform 0.3s ease' }} onMouseEnter={e => e.currentTarget.style.transform = 'translateX(10px)'} onMouseLeave={e => e.currentTarget.style.transform = 'translateX(0)'}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '16px' }}>
                    <div>
                      <h3 style={{ fontSize: '1.4rem', fontWeight: 600, color: '#fff' }}>{rec.name}</h3>
                      <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginTop: '4px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span>📍 {rec.city || 'Bangalore'}</span>
                        {rec.cost_for_two > 0 && (
                          <>
                            <span style={{ color: 'var(--glass-border)' }}>|</span>
                            <span>💰 ₹{rec.cost_for_two} for two</span>
                          </>
                        )}
                      </div>
                    </div>
                    <div style={{ textAlign: 'right' }}>
                      <div style={{ fontSize: '1.2rem', fontWeight: 800, color: '#fbbf24' }}>
                        ★ {rec.rating ? rec.rating.toFixed(1) : '4.5+'}
                      </div>
                      <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>{prefs.budget} Budget</div>
                    </div>
                  </div>
                  <p style={{ color: 'var(--text-muted)', lineHeight: 1.6, fontSize: '0.95rem', marginBottom: rec.cuisines ? '12px' : '0' }}>
                    {rec.reasoning}
                  </p>
                  {rec.cuisines && rec.cuisines.length > 0 && (
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', marginTop: '12px' }}>
                      {rec.cuisines.map((c, idx) => (
                        <span key={idx} style={{ fontSize: '0.75rem', color: 'var(--text-muted)', background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--glass-border)', padding: '2px 8px', borderRadius: '12px' }}>
                          {c}
                        </span>
                      ))}
                    </div>
                  )}
                  <div style={{ marginTop: '14px' }}>
                    <span style={{ fontSize: '0.8rem', color: 'var(--primary)', background: 'rgba(255, 77, 77, 0.1)', padding: '4px 8px', borderRadius: '4px', display: 'inline-block' }}>
                      Match Score: {(rec.score * 100).toFixed(0)}%
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}

          {!loading && !results && !error && (
            <div className="glass-card" style={{ padding: '100px 40px', textAlign: 'center', opacity: 0.5 }}>
              <p style={{ fontSize: '1.2rem' }}>Fill out your preferences to see AI-powered suggestions.</p>
            </div>
          )}
        </section>
      </main>

      <style>{`
        @keyframes spin { to { transform: rotate(360deg); } }
      `}</style>
    </div>
  );
}

export default App;
