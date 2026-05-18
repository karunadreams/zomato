import { Star, MapPin, Utensils, IndianRupee } from 'lucide-react';
import { motion } from 'framer-motion';

interface RestaurantCardProps {
  name: string;
  rating: number;
  cuisines: string[];
  cost_for_two: number;
  reasoning: string;
  score: number;
  city: string;
}

export default function RestaurantCard({ 
  name, rating, cuisines, cost_for_two, reasoning, score, city 
}: RestaurantCardProps) {
  return (
    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ y: -5 }}
      className="bg-card border border-card-border rounded-xl p-6 shadow-sm hover:shadow-md transition-all"
    >
      <div className="flex justify-between items-start mb-4">
        <div className="flex-1">
          <h3 className="text-xl font-bold text-foreground mb-1">{name}</h3>
          <div className="flex items-center text-muted text-sm gap-4">
            <span className="flex items-center gap-1">
              <MapPin className="w-3 h-3" /> {city}
            </span>
            {cost_for_two > 0 && (
              <span className="flex items-center gap-1">
                <IndianRupee className="w-3 h-3" /> {cost_for_two} for two
              </span>
            )}
          </div>
        </div>
        <div className="bg-gold/10 text-gold px-3 py-1 rounded-lg flex items-center gap-1 font-bold">
          <Star className="w-4 h-4 fill-current" />
          {rating}
        </div>
      </div>

      <div className="flex flex-wrap gap-2 mb-4">
        {cuisines.map((c, i) => (
          <span key={i} className="px-3 py-1 bg-background border border-card-border text-muted text-xs rounded-full">
            {c}
          </span>
        ))}
      </div>

      <p className="text-sm text-muted leading-relaxed mb-4">
        {reasoning}
      </p>

      <div className="mt-4 flex justify-between items-center text-[10px] uppercase tracking-wider font-bold text-muted/50">
        <span>Personalized Match</span>
        <span className="text-primary">{(score * 100).toFixed(0)}%</span>
      </div>
    </motion.div>
  );
}
