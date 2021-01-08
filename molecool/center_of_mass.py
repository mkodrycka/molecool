def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
    
    Parameters
    ----------
    symbols : list
        A list of elements.
    
    Returns
    -------
    mass : float
        The mass of the molecule
    """

    mass = 0
    for atom in symbols:
        mass += atomic_weights[atom]
    
    return mass

def calculate_center_of_mass(symbols, coordinates):
   """Calculate the center of mass of a molecule.
   
   The center of mass is weighted by each atom's weight.
   
   Parameters
   ----------
   symbols : list
       A list of elements for the molecule
   coordinates : np.ndarray
       The coordinates of the molecule.
   
   Returns
   -------
   center_of_mass: np.ndarray
       The center of mass of the molecule.

   Notes
   -----
   The center of mass is calculated with the formula
   
   .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
   
   """

   total_mass = calculate_molecular_mass(symbols)
   
   mass_array = np.zeros([len(symbols), 1])
   
   for i in range(len(symbols)):
       mass_array[i] = atom_weights[symbols[i]]
   
   center_of_mass = sum(coordinates * mass_array) / total_mass
   
   return center_of_mass
