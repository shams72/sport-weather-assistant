import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import SearchField from './components/SearchField'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <>    
    <SearchField />
    </>
  </StrictMode>,
)
