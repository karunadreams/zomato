---
name: Culinary Pulse
colors:
  surface: '#faf9f9'
  surface-dim: '#dbdad9'
  surface-bright: '#faf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e8'
  surface-container-highest: '#e3e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#5b403f'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#8f6f6e'
  outline-variant: '#e4bebc'
  surface-tint: '#bb162c'
  primary: '#b7122a'
  on-primary: '#ffffff'
  primary-container: '#db313f'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb3b1'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#785600'
  on-tertiary: '#ffffff'
  tertiary-container: '#976d00'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3b1'
  on-primary-fixed: '#410007'
  on-primary-fixed-variant: '#92001c'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#ffdea6'
  tertiary-fixed-dim: '#ffbb0c'
  on-tertiary-fixed: '#271900'
  on-tertiary-fixed-variant: '#5d4200'
  background: '#faf9f9'
  on-background: '#1b1c1c'
  surface-variant: '#e3e2e2'
  status-green: '#24963F'
  status-gold: '#F4C430'
  surface-off-white: '#F8F8F8'
  border-light: '#E8E8E8'
typography:
  headline-xl:
    fontFamily: Metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Metropolis
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Metropolis
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Metropolis
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Metropolis
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-bold:
    fontFamily: Metropolis
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 16px
  label-sm:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 14px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1200px
  gutter: 1.5rem
  margin-mobile: 1rem
  margin-desktop: 2.5rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 2rem
---

## Brand & Style

The design system is centered on the concept of "Vibrant Utility"—a high-energy, appetizing interface that prioritizes speed and visual delight. It targets food enthusiasts who value both discovery and convenience. 

The aesthetic leans into **Corporate Modern with a Minimalist edge**, utilizing heavy whitespace to let high-resolution food photography act as the primary visual driver. By combining a "Zomato Red" primary palette with generous negative space and soft, tactile elevations, the system evokes a sense of freshness and reliability. The interface is intentionally "airy," reducing cognitive load in information-dense environments like restaurant listings and menu grids.

## Colors

The palette is dominated by the primary red, used strategically for calls to action, brand identifiers, and interactive states. 

- **Primary Red (#E23744):** Reserved for high-priority actions and branding. 
- **Secondary Slate (#1C1C1C):** Used for primary headings and high-contrast text to ensure legibility.
- **Surface Strategy:** The UI utilizes a "pure white" (#FFFFFF) base for primary canvases, with "Off-White" (#F8F8F8) used for background sections to distinguish between layout containers.
- **Status Colors:** Functional accents include a vibrant green for operational status (Open/Available) and a warm gold for qualitative metrics like ratings and reviews.

## Typography

This design system uses a single-family approach with **Metropolis** to maintain a clean, contemporary, and geometric feel. 

Hierarchy is established through weight and scale rather than font switching. Large headlines (XL and LG) should always use bold weights with tighter letter spacing to create a strong visual anchor. Body copy defaults to 16px for optimal readability across devices. Labels utilize medium and semi-bold weights at smaller sizes to ensure they don't get lost in information-dense components like filter chips and restaurant tags.

## Layout & Spacing

The layout follows a **Fluid Grid** model with a hard-capped max-width for desktop to ensure content remains digestible. 

- **Desktop:** 12-column grid with 24px gutters. Use wide margins (40px+) to maintain the "airy" feel.
- **Mobile:** Single-column flow with 16px side margins. 
- **Spacing Rhythm:** Based on a 4px baseline. Components should generally use 8px (sm), 16px (md), or 32px (lg) increments for internal padding and external margins to maintain a consistent vertical rhythm. Large gaps between sections (48px-64px) are encouraged to emphasize discovery categories.

## Elevation & Depth

Visual depth in this design system is achieved through **Ambient Shadows and Tonal Layers**. 

1.  **Level 0 (Surface):** The main background, typically White or Off-White.
2.  **Level 1 (Cards/Inputs):** Subtle, highly diffused shadows (e.g., 0px 4px 20px rgba(0,0,0,0.05)) are used to lift restaurant cards and search bars from the surface.
3.  **Level 2 (Hover/Active):** When a card is hovered, the shadow deepens slightly and the card may scale by 1-2% to provide tactile feedback.
4.  **Level 3 (Overlays/Modals):** Stronger shadows with a 15% opacity backdrop blur to create a glass-like separation for filters and mobile menus.

Avoid heavy borders; use subtle #E8E8E8 outlines only when a clear separation is required on identical-color backgrounds.

## Shapes

The shape language is friendly and organic. 

- **Base Radius:** 8px (0.5rem) for smaller elements like buttons and input fields.
- **Large Radius:** 12px-16px (0.75rem - 1rem) for restaurant cards, modal containers, and hero imagery to soften the overall visual impact.
- **Pill Shapes:** Used exclusively for tags, badges, and filter chips to distinguish them as interactive, selectable elements.
- **Photography:** All food images must have a minimum 12px corner radius to align with the UI's rounded character.

## Components

- **Buttons:** Primary buttons use the Zomato Red background with white text and 8px corners. Secondary buttons use a transparent background with a Red border.
- **Searchable Headers:** Large, prominent search bars with integrated location selection. Use a "Level 1" shadow and 12px roundedness to make it the focal point of the landing page.
- **Filter Chips:** Pill-shaped with a light gray stroke. Active states should fill with a subtle red tint or solid Red for high visibility.
- **Restaurant Cards:** The core component. 16px corner radius, top-aligned image (aspect ratio 4:3), followed by a headline, rating badge (Gold background), and subtext (cuisine/price) in slate gray.
- **Checkboxes & Radios:** Should be slightly larger than standard (20px) with rounded corners and Primary Red fill for selected states.
- **Lists:** Clean, border-less rows separated by subtle 1px horizontal rules in `#E8E8E8`.