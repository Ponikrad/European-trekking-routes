# Top Trekking Routes in Europe - Data Analytics Project

## Project Overview

Ten projekt to kompleksowa analiza 50 najbardziej ikonicznych tras trekkingowych w Europie. Celem było zbadanie korelacji między trudnością trasy, przewyższeniem (elevation gain) a ocenami użytkowników, aby zidentyfikować "najbardziej wymagające" oraz "najbardziej satysfakcjonujące" szlaki na kontynencie.

** Link do interaktywnego Dashboardu:** [Tableau Public - European Trekking Routes](https://public.tableau.com/views/Europeantrekkingroutes/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Tech Stack

- **Data Cleaning & Processing:** Python (Pandas)
- **Data Visualization:** Tableau Public
- **Source Data:** AllTrails, Hiking Project, and official trail guides (Consolidated Dataset).

## Data Processing Workflow

Projekt wymagał zaawansowanego przygotowania danych, ponieważ pierwotne zbiory były niekompletne lub ograniczone geograficznie.

1.  **Data Extraction:** Konsolidacja danych technicznych dla 50 tras (dystans, przewyższenie, oceny).
2.  **Feature Engineering (Python):** \* Stworzenie **Effort Index** ($Elevation Gain / Distance$), aby obiektywnie zmierzyć stromość tras.
    - Kategoryzacja tras na: _Day Trip_, _Multi-day_, oraz _Thru-hike_.
3.  **Data Normalization:** Rozbicie tras przebiegających przez wiele państw (np. Tour du Mont Blanc) na osobne rekordy (funkcja `.explode()` w Pandas), aby umożliwić poprawną wizualizację na mapie Tableau.

## Key Insights

- **Stromość vs Trudność:** Trasy o najwyższym wskaźniku wysiłku (Effort Index) nie zawsze są najdłuższe (np. Orla Perć w Polsce czy Hardergrat w Szwajcarii).
- **Top Regiony:** Alpy i Skandynawia dominują w rankingu najwyżej ocenianych szlaków (średni Rating > 4.8).
- **Dostępność:** Analiza wykazała, że popularność szlaku często zależy bardziej od jego "ikoniczności" (np. Preikestolen) niż od poziomu trudności.

## Project Structure

- `/data` - zawiera pliki CSV.
- `/dashboard` - screenshot Dashboardu.
- `README.md` - opis projektu.
