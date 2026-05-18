"use client";

import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, Sliders, Loader2, UtensilsCrossed, AlertCircle, Sparkles } from 'lucide-react';
import RestaurantCard from '@/components/RestaurantCard';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://127.0.0.1:8000';

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

export default function Home() {
  const [prefs, setPrefs] = useState({
    city: '',
    budget: 'Low',
    cuisines: '',
    min_rating: 0.0,
    additional_context: ''
  });
  const [results, setResults] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
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
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`min-h-screen pb-20 pt-10 px-4 flex flex-col transition-all duration-500 ease-out ${results || loading || error ? 'justify-start' : 'justify-center'}`}>
      <div className="max-w-2xl mx-auto w-full">
        
        {/* Unified Experience Card */}
        <motion.div 
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          className="bg-card rounded-[2rem] border border-card-border shadow-2xl shadow-black/40 overflow-hidden"
        >
          {/* Header Section inside Card */}
          <div className="bg-primary/5 p-6 text-center border-b border-card-border">
            <motion.div 
              initial={{ scale: 0.9, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              className="flex justify-center mb-2"
            >
              <div className="bg-primary p-2 rounded-2xl shadow-lg shadow-primary/20">
                <UtensilsCrossed className="text-white w-5 h-5" />
              </div>
            </motion.div>
            <h1 className="text-3xl md:text-4xl font-black text-foreground tracking-tight">
              Find the perfect place <span className="text-primary italic">to eat.</span>
            </h1>
          </div>

          <div className="p-6 md:p-8">
            <form onSubmit={handleSubmit} className="space-y-6">
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Locality Search */}
                <div className="md:col-span-1">
                  <label className="block text-xs font-bold uppercase tracking-widest text-muted mb-2">Locality</label>
                  <select 
                    className="w-full px-4 py-3 bg-background border-2 border-card-border rounded-xl text-md font-medium focus:outline-none focus:border-primary transition-all cursor-pointer"
                    value={prefs.city} 
                    onChange={e => setPrefs({...prefs, city: e.target.value})}
                  >
                    <option value="">All Localities (Bangalore)</option>
                    {LOCALITIES.map(loc => (
                      <option key={loc} value={loc}>
                        {loc}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Budget Band */}
                <div className="md:col-span-1">
                  <label className="block text-xs font-bold uppercase tracking-wider text-muted mb-2">Budget Band</label>
                  <div className="grid grid-cols-3 gap-2 h-[52px]">
                    {['Low', 'Medium', 'High'].map(b => (
                      <button
                        key={b}
                        type="button"
                        onClick={() => setPrefs({...prefs, budget: b})}
                        className={`py-2 text-xs font-bold rounded-xl border transition-all ${
                          prefs.budget === b 
                            ? 'bg-primary border-primary text-white shadow-md shadow-primary/20' 
                            : 'bg-card border-card-border text-muted hover:border-primary/50'
                        }`}
                      >
                        {b}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Cuisines */}
                <div className="md:col-span-1">
                  <label className="block text-xs font-bold uppercase tracking-wider text-muted mb-2">Cuisines</label>
                  <input 
                    className="w-full px-4 py-3 bg-background border border-card-border rounded-xl text-sm focus:outline-none focus:border-primary transition-colors"
                    value={prefs.cuisines} 
                    onChange={e => setPrefs({...prefs, cuisines: e.target.value})}
                    placeholder="e.g. Italian, Chinese"
                  />
                </div>

                {/* Min Rating */}
                <div className="md:col-span-1 flex flex-col justify-center">
                  <label className="block text-xs font-bold uppercase tracking-wider text-yellow-500 mb-2">
                    Min Rating <span className="text-yellow-600 font-bold">({prefs.min_rating}+)</span>
                  </label>
                  <input 
                    type="range" min="0" max="5" step="0.1"
                    className="w-full h-2 bg-gray-200 rounded-lg cursor-pointer accent-primary mt-2"
                    value={prefs.min_rating} 
                    onChange={e => setPrefs({...prefs, min_rating: parseFloat(e.target.value)})}
                  />
                </div>
                
                {/* Additional Context */}
                <div className="md:col-span-2">
                  <label className="block text-xs font-bold uppercase tracking-wider text-muted mb-2">Additional Context</label>
                  <input 
                    className="w-full px-4 py-3 bg-background border border-card-border rounded-xl text-sm focus:outline-none focus:border-primary transition-colors"
                    value={prefs.additional_context} 
                    onChange={e => setPrefs({...prefs, additional_context: e.target.value})}
                    placeholder="e.g. Pet-friendly spots, outdoor seating"
                  />
                </div>
              </div>

              <div className="pt-2">
                <button 
                  type="submit" 
                  className="w-full bg-primary hover:bg-primary-hover text-white font-bold py-4 rounded-xl shadow-lg shadow-primary/30 transition-all active:scale-[0.98] disabled:opacity-50 text-lg tracking-tight"
                  disabled={loading}
                >
                  {loading ? (
                    <div className="flex items-center justify-center gap-3">
                      <Loader2 className="w-5 h-5 animate-spin" />
                      <span>Analyzing Data...</span>
                    </div>
                  ) : 'Get Recommendations'}
                </button>
              </div>
            </form>
          </div>
        </motion.div>

        {/* Results Area */}
        <div className="mt-20 max-w-3xl mx-auto">
          <AnimatePresence mode="wait">
            {loading && (
              <motion.div 
                key="loading"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="flex flex-col items-center justify-center py-24 text-center"
              >
                <div className="relative mb-6">
                  <Loader2 className="w-12 h-12 text-primary animate-spin" />
                  <Sparkles className="absolute -top-2 -right-2 w-6 h-6 text-gold animate-bounce" />
                </div>
                <h3 className="text-xl font-bold mb-2 text-primary">Curating Your Perfect List</h3>
                <p className="text-muted">Analyzing {prefs.city} restaurant reviews...</p>
              </motion.div>
            )}

            {error && (
              <motion.div 
                key="error"
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                className="bg-card border border-red-500/20 p-8 rounded-2xl text-center shadow-lg"
              >
                <AlertCircle className="w-12 h-12 text-primary mx-auto mb-4" />
                <h3 className="text-xl font-bold mb-2">No Matches Found</h3>
                <p className="text-muted mb-6">{error}</p>
                <button 
                  onClick={() => setError(null)}
                  className="bg-primary/10 text-primary px-6 py-2 rounded-full font-bold text-sm hover:bg-primary/20 transition-colors"
                >
                  Adjust Filters
                </button>
              </motion.div>
            )}

            {results && (
              <motion.div 
                key="results"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="space-y-8"
              >
                <div className="bg-card p-8 rounded-2xl border border-card-border border-l-4 border-l-green italic text-muted text-lg leading-relaxed shadow-sm">
                  "{results.summary}"
                </div>
                <div className="grid grid-cols-1 gap-8">
                  {results.recommendations.map((rec: any, i: number) => (
                    <RestaurantCard 
                      key={i} 
                      {...rec} 
                      city={rec.city || prefs.city || 'Bangalore'} 
                      cuisines={rec.cuisines || []} 
                      cost_for_two={rec.cost_for_two || 0}
                      rating={rec.rating || 4.0}
                    />
                  ))}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </div>
    </div>
  );
}
