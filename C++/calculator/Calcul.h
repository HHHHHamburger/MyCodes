// Calcul.h : main header file for the CALCUL application
//

#if !defined(AFX_CALCUL_H__17FC1FF4_8F6A_4FA7_A80C_A005F81F2DE0__INCLUDED_)
#define AFX_CALCUL_H__17FC1FF4_8F6A_4FA7_A80C_A005F81F2DE0__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CCalculApp:
// See Calcul.cpp for the implementation of this class
//

class CCalculApp : public CWinApp
{
public:
	CCalculApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CCalculApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CCalculApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_CALCUL_H__17FC1FF4_8F6A_4FA7_A80C_A005F81F2DE0__INCLUDED_)
